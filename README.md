# Eye-drowsiness-Detection-System

A real time eye drowsiness detection system built using Python and Computer Vision that detects prolonged eye closure and triggers an alarm to prevent accidents caused by driver fatigue.
This project is designed for road safety, but it can also be adapted for workplace monitoring, study fatigue alerts, or health monitoring systems.

🔍 Problem Statement
Driver drowsiness is one of the major causes of road accidents, especially during night driving or long journeys.
When a driver’s eyes remain closed for a few seconds, the risk of accidents increases drastically.

👉 Goal:
Detect eye closure in real time and alert the user before a dangerous situation occurs.

💡 Solution Overview
This system:
Captures live video from a webcam
Detects the face and eyes
Determines whether eyes are OPEN or CLOSED
Measures how long the eyes remain closed
Triggers a loud alarm/siren if drowsiness is detected

⚙️ How It Works (Simple Flow)
Webcam captures live video
Face is detected from each frame
Facial landmarks are extracted
Eye Aspect Ratio (EAR) is calculated

If EAR stays below a threshold for a fixed time:
🚨 Alarm is triggered
Alarm stops once eyes open again

🧠 Key Concept – Eye Aspect Ratio (EAR)
The Eye Aspect Ratio (EAR) is a geometric measure that helps determine whether an eye is open or closed.
High EAR → Eyes Open
Low EAR → Eyes Closed
By tracking EAR across multiple frames, we reliably detect drowsiness instead of blinking.

✨ Features
! Real-time eye detection
! Accurate drowsiness detection
! Alarm / siren alert system
! Works in normal lighting conditions
! Lightweight & fast execution
 
Can be extended for:
Car safety systems
Study reminders
Office fatigue monitoring

🛠️ Tech Stack
Language: Python 3

Libraries Used:
OpenCV
MediaPipe / dlib (facial landmarks)
NumPy
Playsound / Pygame (for alarm)

📁 Project Structure
eye-drowsiness-detection/
│
├── drowsiness_detection.py   # Main program
├── alarm.wav                 # Alarm sound
├── requirements.txt          # Dependencies
├── README.md                 # Project documentation
└── assets/                   # (Optional) images or demo files


You can fine-tune:
Eye closure time threshold (e.g. 2–3 seconds)
EAR threshold value
Alarm sound & volume
This makes the system adaptable for different users and environments.

🚀 Future Improvements
Add mobile app integration
Use deep learning eye-state classifier
Integrate with ESP32 / IoT modules
Night-time IR camera support
Driver behavior analytics dashboard

🎓 Use Cases

🚘 Driver drowsiness prevention

📚 Study fatigue alert system

🧑‍💻 Office employee monitoring

🏭 Industrial safety monitoring

👨‍💻 Author
Sarthak Bhopale
Aspiring Engineer | Python & Computer Vision Developer
Passionate about building real-world safety systems

📜 License
This project is Open Sourced and Can be used for educational Activities.
You are free to use, modify, and distribute it.
