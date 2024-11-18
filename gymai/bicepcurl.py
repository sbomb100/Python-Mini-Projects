import cv2
import mediapipe as mp
import numpy as np
import matplotlib.pyplot as plt
import time

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Data storage for analysis
timestamps = []
angles = []
wrist_positions = []

# Function to calculate angle between three points
def calculate_angle(a, b, c):
    """
    Calculate the angle between three points:
    a: shoulder
    b: elbow
    c: wrist
    """
    a = np.array(a)  # Shoulder
    b = np.array(b)  # Elbow
    c = np.array(c)  # Wrist

    # Calculate vectors
    ba = a - b
    bc = c - b

    # Calculate cosine of angle
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(np.clip(cosine_angle, -1.0, 1.0))
    return np.degrees(angle)

# Initialize Video Capture
cap = cv2.VideoCapture(0)

print("Perform a bicep curl to record data... Press 'q' to stop.")
start_time = time.time()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert image to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    # Draw pose landmarks
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Extract key points
        landmarks = results.pose_landmarks.landmark

        # Get coordinates for the shoulder, elbow, and wrist (right side)
        right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                          landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
        right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                       landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
        right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                       landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

        # Calculate angle
        angle = calculate_angle(right_shoulder, right_elbow, right_wrist)
        angles.append(angle)

        # Record wrist height
        wrist_positions.append(right_wrist[1])  # Y-axis represents height
        timestamps.append(time.time() - start_time)

        # Display angle on the frame
        cv2.putText(frame, f"Angle: {int(angle)} degrees", 
                    (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Show the frame
    cv2.imshow('Bicep Curl Tracker', frame)

    # Exit with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Plot the results
plt.figure(figsize=(10, 5))

# Plot angle over time
plt.subplot(2, 1, 1)
plt.plot(timestamps, angles, label="Elbow Angle")
plt.xlabel("Time (s)")
plt.ylabel("Angle (degrees)")
plt.title("Bicep Curl Angle Over Time")
plt.legend()

# Plot wrist vertical movement
plt.subplot(2, 1, 2)
plt.plot(timestamps, wrist_positions, label="Wrist Height (y-coordinate)", color="orange")
plt.xlabel("Time (s)")
plt.ylabel("Wrist Position (normalized)")
plt.title("Wrist Movement During Bicep Curl")
plt.legend()

plt.tight_layout()
plt.show()