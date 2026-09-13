import cv2
import numpy as np

# -----------------------------
# CAMERA SETUP
# -----------------------------

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()


# -----------------------------
# BACKGROUND BUFFER
# -----------------------------

background = None

# EMA learning rate
# Smaller = slower, more stable background
alpha = 0.05


# -----------------------------
# MAIN LOOP
# -----------------------------

while True:

    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame")
        break

    # Mirror camera
    frame = cv2.flip(frame, 1)

    # Convert frame to float32
    current = frame.astype(np.float32)


    # -----------------------------
    # INITIALIZE BACKGROUND
    # -----------------------------

    if background is None:

        background = current.copy()

        print("Background initialized automatically.")


    # -----------------------------
    # TEMPORARY MASK
    # -----------------------------
    #
    # Step 3 will replace this with
    # the actual cloak-color mask.
    #
    # For now, there is no cloak.
    #

    mask = np.zeros(frame.shape[:2], dtype=np.uint8)


    # -----------------------------
    # UPDATE BACKGROUND
    # -----------------------------

    if background is not None:

        # Pixels where there is NO cloak
        non_cloak = mask == 0

        background[non_cloak] = (
            (1 - alpha) * background[non_cloak]
            + alpha * current[non_cloak]
        )


    # -----------------------------
    # CONVERT BACK TO IMAGE
    # -----------------------------

    background_display = np.clip(
        background,
        0,
        255
    ).astype(np.uint8)


    # -----------------------------
    # DISPLAY
    # -----------------------------

    cv2.imshow("Live Camera", frame)

    cv2.imshow(
        "Continuous Background",
        background_display
    )


    # -----------------------------
    # EXIT
    # -----------------------------

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break


# -----------------------------
# CLEANUP
# -----------------------------

cap.release()
cv2.destroyAllWindows()