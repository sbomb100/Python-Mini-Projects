import cv2
import mediapipe as mp

# Initialize MediaPipe Hand tracking module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize OpenCV to access the webcam
cap = cv2.VideoCapture(0)

def is_flipping_off(hand_landmarks):
    # Get the positions of the fingers
    thumb_tip = hand_landmarks.landmark[4]
    index_tip = hand_landmarks.landmark[8]
    middle_tip = hand_landmarks.landmark[12]
    ring_tip = hand_landmarks.landmark[16]
    pinky_tip = hand_landmarks.landmark[20]

    # Check if the middle finger is extended and other fingers are curled
    if (middle_tip.y < hand_landmarks.landmark[9].y and  # Check if middle finger is extended
        index_tip.y < hand_landmarks.landmark[6].y and  # Index is down
        ring_tip.y > hand_landmarks.landmark[14].y and  # Ring finger is curled
        pinky_tip.y > hand_landmarks.landmark[18].y):   # Pinky is curled
        return True
    return False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later mirror display
    frame = cv2.flip(frame, 1)
    
    # Convert the frame to RGB for MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to find hands
    results = hands.process(rgb_frame)

    # Draw landmarks if hands are detected
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Draw the landmarks on the frame
            mp.solutions.drawing_utils.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
            if is_flipping_off(landmarks):
                cv2.putText(frame, "Flipping off detected!", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,225), 2)

    # Display the frame
    cv2.imshow('Hand Gesture Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



# Release the capture and close the window
cap.release()
cv2.destroyAllWindows()