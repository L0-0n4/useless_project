import cv2
import numpy as np

# -----------------------------------
# CAMERA SETUP
# -----------------------------------

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()


# -----------------------------------
# RED CLOAK SETTINGS
# -----------------------------------

hue_tolerance = 10
min_saturation = 120
min_value = 60


# -----------------------------------
# MAIN LOOP
# -----------------------------------

while True:

    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame")
        break

    # Mirror camera
    frame = cv2.flip(frame, 1)

    # Convert BGR → HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h, s, v = cv2.split(hsv)


    # -----------------------------------
    # RED COLOR DETECTION
    # -----------------------------------

    # Red exists around BOTH:
    # 0 and 179 in OpenCV HSV

    red_lower = (
        (h <= hue_tolerance) &
        (s > min_saturation) &
        (v > min_value)
    )

    red_upper = (
        (h >= 180 - hue_tolerance) &
        (s > min_saturation) &
        (v > min_value)
    )

    mask = red_lower | red_upper


    # Convert to black/white
    mask = mask.astype(np.uint8) * 255


    # -----------------------------------
    # CLEAN MASK
    # -----------------------------------

    kernel = np.ones((3, 3), np.uint8)

    # Remove tiny noise
    mask = cv2.erode(
        mask,
        kernel,
        iterations=1
    )

    # Restore main regions
    mask = cv2.dilate(
        mask,
        kernel,
        iterations=1
    )


    # -----------------------------------
    # REMOVE SMALL REGIONS
    # -----------------------------------

    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
        mask,
        connectivity=8
    )

    clean_mask = np.zeros_like(mask)

    for i in range(1, num_labels):

        area = stats[i, cv2.CC_STAT_AREA]

        if area > 500:
            clean_mask[labels == i] = 255

    mask = clean_mask


    # -----------------------------------
    # DISPLAY
    # -----------------------------------

    cv2.imshow("Camera", frame)
    cv2.imshow("Red Cloak Mask", mask)


    # -----------------------------------
    # EXIT
    # -----------------------------------

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break


# -----------------------------------
# CLEANUP
# -----------------------------------

cap.release()
cv2.destroyAllWindows()