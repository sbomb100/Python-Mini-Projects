from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Sample keypoint data (X) and labels (y)
X = np.array([
    # Example: keypoints for squats
    [0.1, 0.5, 0.8, 0.3, 0.7],
    # Example: keypoints for push-ups
    [0.2, 0.4, 0.9, 0.2, 0.6],
])
y = ['squat', 'push-up']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest Classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Predict new data
prediction = clf.predict([X_test[0]])
print("Predicted Exercise:", prediction)