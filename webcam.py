import cv2

# Open the webcam
cap = cv2.VideoCapture(0)

# Check if webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam")
    exit()

while True:
    # Read a frame
    ret, frame = cap.read()

    # Check if frame was captured
    if not ret:
        print("Error: Could not read frame")
        break

    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Display the frame
    cv2.imshow("Invisibility Cloak - Webcam", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()