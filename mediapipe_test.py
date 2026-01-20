import cv2
import time
import numpy as np
import mediapipe as mp
import threading
from playsound import playsound
from math import dist
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# ---------------- CONFIG ---------------- #
EYE_AR_THRESH = 0.23
EYE_CLOSED_SECONDS = 2.5
ALARM_SOUND = "alarm.wav"
ALARM_COOLDOWN = 3
MODEL_PATH = "face_landmarker.task"
# ---------------------------------------- #

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

alarm_active = False
last_alarm_time = 0


def sound_alarm():
    global alarm_active
    alarm_active = True
    playsound(ALARM_SOUND)
    alarm_active = False


def eye_aspect_ratio(eye):
    A = dist(eye[1], eye[5])
    B = dist(eye[2], eye[4])
    C = dist(eye[0], eye[3])
    return (A + B) / (2.0 * C)


# Initialize MediaPipe FaceLandmarker
base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.FaceLandmarkerOptions(
    base_options=base_options,
    output_face_blendshapes=False,
    output_facial_transformation_matrixes=False,
    num_faces=1
)

detector = vision.FaceLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)
time.sleep(1)

eye_closed_start = None
frame_count = 0
start_time = time.time()

print("[INFO] Drowsiness Detection Started")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1
    h, w = frame.shape[:2]

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)

    result = detector.detect(mp_image)
    status = "NO FACE"

    if result.face_landmarks:
        landmarks = result.face_landmarks[0]

        left_eye = [(int(landmarks[i].x * w), int(landmarks[i].y * h)) for i in LEFT_EYE]
        right_eye = [(int(landmarks[i].x * w), int(landmarks[i].y * h)) for i in RIGHT_EYE]

        ear = (eye_aspect_ratio(left_eye) + eye_aspect_ratio(right_eye)) / 2.0

        for p in left_eye + right_eye:
            cv2.circle(frame, p, 2, (0, 255, 0), -1)

        if ear < EYE_AR_THRESH:
            if eye_closed_start is None:
                eye_closed_start = time.time()

            elapsed = time.time() - eye_closed_start
            status = "EYES CLOSED"

            if elapsed >= EYE_CLOSED_SECONDS:
                status = "DROWSY!"

                if not alarm_active and (time.time() - last_alarm_time) > ALARM_COOLDOWN:
                    last_alarm_time = time.time()
                    threading.Thread(target=sound_alarm, daemon=True).start()

                cv2.putText(frame, "WAKE UP!", (10, 120),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
        else:
            eye_closed_start = None
            status = "EYES OPEN"

    fps = frame_count / (time.time() - start_time)

    cv2.putText(frame, f"Status: {status}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)
    cv2.putText(frame, f"FPS: {fps:.1f}", (10, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("Driver Drowsiness Detection ", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
