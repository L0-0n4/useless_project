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
<img width="1600" height="722" alt="WhatsApp Image 2026-09-13 at 4 24 13 PM" src="https://github.com/user-attachments/assets/214ce824-da93-4b27-8092-854a037c65bd" />
Project User Interface

The magical-themed Invisibility Cloak interface provides a dedicated display area for the OpenCV camera feed and presents the project in an interactive, visually appealing format.

<img width="1593" height="817" alt="WhatsApp Image 2026-09-13 at 4 24 13 PM (1)" src="https://github.com/user-attachments/assets/2c2c5944-cb27-47e5-af72-6a4bfedf643d" />

Live Camera Input

The live webcam feed captures the user and the surrounding environment before applying the invisibility effect.

<img width="1600" height="715" alt="WhatsApp Image 2026-09-13 at 4 24 13 PM (2)" src="https://github.com/user-attachments/assets/190e6b7d-906b-4814-badf-74746d5c6ef9" />
Invisibility Effect

The red cloak is detected and replaced with the previously captured background, creating the illusion that the cloak and the covered area have disappeared.

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
https://github.com/user-attachments/assets/94a1866e-c518-4990-a37a-dfe98e59e255

The video demonstrates the working prototype of the Cloak of Invisibility. The application opens through a magical-themed interface and accesses the webcam to capture the live scene. After the background is captured, the system detects the red cloak and replaces the detected area with the captured background, creating the illusion that the person wearing the cloak has disappeared. The video showcases the real-time invisibility effect running on the laptop.

# Additional Demos
[Add any extra demo materials/links]

## Team Contributions
E P Sreenanda: Contributed to the overall project development, including the computer vision implementation, background capture, testing, and integration.

Elizabeth Sebastian:  Designed and developed the magical-themed user interface and contributed to the overall project development, testing, and integration.

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)



