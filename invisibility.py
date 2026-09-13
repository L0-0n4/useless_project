import cv2
import numpy as np


# ============================================================
# CAMERA
# ============================================================

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()


# ============================================================
# CAMERA RESOLUTION
# ============================================================

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)


# ============================================================
# BACKGROUND
# ============================================================

warmup_frames = 75

background = None
frame_count = 0
background_ready = False


# ============================================================
# CLOAK DETECTION SETTINGS
# ============================================================

# HSV settings
MIN_SATURATION = 65
MIN_VALUE = 20


# Minimum size of detected cloak
MIN_CLOAK_AREA = 3000


# ============================================================
# MAIN LOOP
# ============================================================

while True:

    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame")
        break


    # --------------------------------------------------------
    # Mirror camera
    # --------------------------------------------------------

    frame = cv2.flip(frame, 1)


    # --------------------------------------------------------
    # HSV
    # --------------------------------------------------------

    hsv = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2HSV
    )

    h, s, v = cv2.split(hsv)


    # ========================================================
    # RED / MAROON DETECTION
    # ========================================================

    # Normal red
    red1 = cv2.inRange(
        hsv,
        np.array([0, MIN_SATURATION, MIN_VALUE]),
        np.array([12, 255, 255])
    )


    # Dark/magenta red
    red2 = cv2.inRange(
        hsv,
        np.array([160, MIN_SATURATION, MIN_VALUE]),
        np.array([179, 255, 255])
    )


    red_mask = cv2.bitwise_or(
        red1,
        red2
    )


    # ========================================================
    # YCrCb SKIN DETECTION
    # ========================================================

    ycrcb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2YCrCb
    )

    y, cr, cb = cv2.split(ycrcb)


    # --------------------------------------------------------
    # Human skin range
    # --------------------------------------------------------

    skin = (
        (cr >= 133) &
        (cr <= 173) &
        (cb >= 77) &
        (cb <= 135) &
        (y >= 45)
    )


    skin = (
        skin.astype(np.uint8) * 255
    )


    # --------------------------------------------------------
    # Expand skin slightly
    # --------------------------------------------------------

    skin_kernel = np.ones(
        (9, 9),
        np.uint8
    )

    skin = cv2.dilate(
        skin,
        skin_kernel,
        iterations=1
    )


    # ========================================================
    # REMOVE SKIN FROM RED MASK
    # ========================================================

    mask = cv2.bitwise_and(
        red_mask,
        cv2.bitwise_not(skin)
    )


    # ========================================================
    # EXTRA RED DOMINANCE
    # ========================================================

    b, g, r = cv2.split(frame)

    r16 = r.astype(np.int16)
    g16 = g.astype(np.int16)
    b16 = b.astype(np.int16)


    # Strong red pixels
    red_dominant = (
        (r16 > g16 + 20) &
        (r16 > b16 + 5) &
        (s.astype(np.int16) > 65)
    )


    red_dominant = (
        red_dominant.astype(np.uint8) * 255
    )


    # Remove skin from this mask too
    red_dominant = cv2.bitwise_and(
        red_dominant,
        cv2.bitwise_not(skin)
    )


    # Add to main mask
    mask = cv2.bitwise_or(
        mask,
        red_dominant
    )


    # ========================================================
    # REMOVE SKIN ONE FINAL TIME
    # ========================================================

    mask = cv2.bitwise_and(
        mask,
        cv2.bitwise_not(skin)
    )


    # ========================================================
    # MORPHOLOGICAL CLEANING
    # ========================================================

    # Remove tiny noise
    kernel_open = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE,
        (5, 5)
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernel_open,
        iterations=1
    )


    # ========================================================
    # CONNECT CLOAK PIECES
    # ========================================================

    # Large kernel because the cloak has dark areas,
    # shadows and small holes.
    kernel_close = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE,
        (17, 17)
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_CLOSE,
        kernel_close,
        iterations=3
    )


    # ========================================================
    # FIND CONNECTED COMPONENTS
    # ========================================================

    num_labels, labels, stats, centroids = (
        cv2.connectedComponentsWithStats(
            mask,
            connectivity=8
        )
    )


    # ========================================================
    # KEEP ONLY THE LARGEST RED OBJECT
    # ========================================================

    largest_area = 0
    largest_label = 0

    for i in range(1, num_labels):

        area = stats[
            i,
            cv2.CC_STAT_AREA
        ]

        if area > largest_area:

            largest_area = area
            largest_label = i


    clean_mask = np.zeros_like(mask)


    if largest_area > MIN_CLOAK_AREA:

        clean_mask[
            labels == largest_label
        ] = 255


    mask = clean_mask


    # ========================================================
    # FILL HOLES INSIDE CLOAK
    # ========================================================

    # Find contours
    contours, hierarchy = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )


    filled_mask = np.zeros_like(mask)


    if len(contours) > 0:

        # Largest contour
        largest_contour = max(
            contours,
            key=cv2.contourArea
        )

        area = cv2.contourArea(
            largest_contour
        )


        if area > MIN_CLOAK_AREA:

            cv2.drawContours(
                filled_mask,
                [largest_contour],
                -1,
                255,
                thickness=cv2.FILLED
            )


    mask = filled_mask


   # ========================================================
# EXPAND MASK TO REMOVE RED OUTLINE
# ========================================================

# Expand the mask outward so the actual red border
# is also covered by the background.

    expand_kernel = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE,
        (21, 21)
    )

    mask = cv2.dilate(
        mask,
        expand_kernel,
        iterations=2
    )


# ========================================================
# SMOOTH EDGES
# ========================================================

    mask = cv2.GaussianBlur(
        mask,
        (7, 7),
        0
    )


    # ========================================================
    # BACKGROUND WARM-UP
    # ========================================================

    if not background_ready:

        current = frame.astype(
            np.float32
        )


        if background is None:

            background = current.copy()

        else:

            background = (
                0.90 * background +
                0.10 * current
            )


        frame_count += 1


        # ----------------------------------------------------
        # Warmup display
        # ----------------------------------------------------

        result = frame.copy()


        cv2.putText(
            result,
            "Preparing background...",
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )


        cv2.putText(
            result,
            "Please stay out of the camera view",
            (30, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )


        remaining = (
            warmup_frames -
            frame_count
        )


        cv2.putText(
            result,
            f"Frames remaining: {max(remaining, 0)}",
            (30, 125),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )


        # Display
        cv2.imshow(
            "Red Invisibility Cloak",
            result
        )


        cv2.imshow(
            "Red Cloak Mask",
            mask
        )


        # ----------------------------------------------------
        # Freeze background
        # ----------------------------------------------------

        if frame_count >= warmup_frames:

            background = np.clip(
                background,
                0,
                255
            ).astype(np.uint8)

            background_ready = True

            print(
                "Background captured and frozen."
            )

            print(
                "You can now enter the camera view."
            )


        # ----------------------------------------------------
        # Exit
        # ----------------------------------------------------

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break

        continue


    # ========================================================
    # INVISIBILITY EFFECT
    # ========================================================

    result = frame.copy()


    # --------------------------------------------------------
    # Use soft mask instead of hard mask
    # --------------------------------------------------------

    alpha = mask.astype(
        np.float32
    ) / 255.0


    # Make 3-channel alpha
    alpha = cv2.merge(
        [alpha, alpha, alpha]
    )


    # Background as float
    background_float = background.astype(
        np.float32
    )


    frame_float = frame.astype(
        np.float32
    )


    # --------------------------------------------------------
    # Blend foreground and background
    # --------------------------------------------------------

    result_float = (
        frame_float * (1 - alpha) +
        background_float * alpha
    )


    result = np.clip(
        result_float,
        0,
        255
    ).astype(np.uint8)


    # ========================================================
    # DISPLAY
    # ========================================================

    cv2.imshow(
        "Red Invisibility Cloak",
        result
    )


    cv2.imshow(
        "Red Cloak Mask",
        mask
    )


    # ========================================================
    # EXIT
    # ========================================================

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break


# ============================================================
# CLEANUP
# ============================================================

cap.release()

cv2.destroyAllWindows()