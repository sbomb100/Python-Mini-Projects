import cv2
import mediapipe as mp
#from ml import clf

# pose: Shoulders Elbows Wrists Hips Knees
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

camera = cv2.VideoCapture(0)

while camera.isOpened():
    ret, frame = camera.read()
    if not ret:
        break

    # Convert the image to RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    # Draw pose landmarks
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        keypoints = [(lm.x, lm.y, lm.z) for lm in results.pose_landmarks.landmark]
        #prediction = clf.predict([keypoints])
        #print("Predicted Exercise:", prediction)

    # Show the frame
    cv2.imshow('Exercise Detector', frame)

    # Exit with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()