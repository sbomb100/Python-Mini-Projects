import cv2
import mediapipe as mp
import csv
import time

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Initialize Video Capture
cap = cv2.VideoCapture(0)

# CSV File Setup
filename = f"exercise_data_{int(time.time())}.csv"
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    header = ['time'] + [f'{part}_{coord}' for part in [
        'left_shoulder', 'right_shoulder', 'left_elbow', 'right_elbow',
        'left_wrist', 'right_wrist', 'left_hip', 'right_hip',
        'left_knee', 'right_knee', 'left_ankle', 'right_ankle'
    ] for coord in ['x', 'y', 'z']]
    writer.writerow(header)

    print(f"Recording coordinates to {filename}...")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        # Draw pose landmarks
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Extract keypoints
            keypoints = []
            for lm in results.pose_landmarks.landmark:
                keypoints.extend([lm.x, lm.y, lm.z])

            # Write data with timestamp
            writer.writerow([time.time()] + keypoints)

        # Show the frame
        cv2.imshow('Pose Recording', frame)

        # Exit with 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()