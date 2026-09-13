<img width="1280" height="640" alt="git (1)" src="https://github.com/user-attachments/assets/8920b256-2ba8-4988-b824-5351134eb4bd" />



# Invisibilty Cloak 🎯


## Basic Details
### Team Name: 23/24


### Team Members
- Team Lead: Elizabeth Sebastian - MACE
- Member 2: E P Sreenanda - MACE

### Project Description
Cloak of Invisibility is a real-time computer vision project built with Python and OpenCV that creates an invisibility effect by detecting a red cloak. The system captures the background at the beginning and uses it to replace the detected cloak area, making the person appear invisible.

### The Problem (that doesn't exist)
People are constantly worried about being seen when they could simply become invisible. Our project solves this completely unnecessary problem by using computer vision to make anyone wearing a red cloak magically disappear from the camera view.

### The Solution (that nobody asked for)
We use Python and OpenCV magic to detect the red cloak and replace it with a previously captured background. Put on the cloak, face the camera, and—poof! You disappear, proving once again that technology can solve problems nobody actually had.

## Technical Details
### Technologies/Components Used
For Software:
Language: Python
Framework: None
Libraries: OpenCV (cv2), NumPy
Tools: Visual Studio Code, Git, GitHub

For Hardware:
Main Components: Laptop/PC, Webcam, Red cloak/cloth
Specifications: Any standard webcam capable of capturing real-time video; laptop/PC capable of running Python and OpenCV
Tools Required: Webcam, computer/laptop, red cloak or red cloth

### Implementation
For Software:
# Installation
pip install opencv-python numpy

# Run
python invisibility.py

### Project Documentation
For Software:

webcam.py – Handles webcam video capture and display.
invisibility.py – Main program that captures the background, detects the red cloak, and creates the invisibility effect.
index.html – Provides the magical-themed user interface for the project.
OpenCV – Used for real-time video processing, color detection, masking, and background replacement.
NumPy – Used for image and pixel-level array operations.

# Screenshots (Add at least 3)
![Screenshot1](Add screenshot 1 here with proper name)
*Add caption explaining what this shows*

![Screenshot2](Add screenshot 2 here with proper name)
*Add caption explaining what this shows*

![Screenshot3](Add screenshot 3 here with proper name)
*Add caption explaining what this shows*

# Diagrams
        ┌──────────────┐
        │    Webcam    │
        └──────┬───────┘
               ↓
     ┌───────────────────┐
     │ Capture Background│
     └─────────┬─────────┘
               ↓
     ┌───────────────────┐
     │   Live Video Feed │
     └─────────┬─────────┘
               ↓
     ┌───────────────────┐
     │ Detect Red Cloak  │
     └─────────┬─────────┘
               ↓
     ┌───────────────────┐
     │ Create Cloak Mask │
     └─────────┬─────────┘
               ↓
     ┌───────────────────┐
     │ Replace Mask Area │
     │ with Background   │
     └─────────┬─────────┘
               ↓
        ┌──────────────┐
        │   Invisible  │
        │    Effect    │
        └──────────────┘
The workflow begins by capturing the background through the webcam. The system then continuously processes the live video, detects the red cloak using color-based segmentation, creates a mask for the detected area, and replaces the masked region with the captured background to produce the final invisibility effect.

### Project Demo
# Video
[Add your demo video link here]
*Explain what the video demonstrates*

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions
E P Sreenanda: Contributed to the overall project development, including the computer vision implementation, background capture, testing, and integration.
Elizabeth Sebastian:  Designed and developed the magical-themed user interface and contributed to the overall project development, testing, and integration.

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)



