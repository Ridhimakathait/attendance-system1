import cv2
import numpy as np
from tensorflow.keras.models import load_model  # type: ignore
import sqlite3
from datetime import datetime
from preprocess import preprocess_images

# Load the model
model = load_model("face_recognition_model.h5")

# Load label dictionary
_, _, label_dict = preprocess_images(r"C:\Users\hp\Downloads\archive\lfw-deepfunneled\lfw-deepfunneled\lfw-deepfunneled")

# Set up SQLite database
conn = sqlite3.connect('attendance.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY,
        name TEXT,
        timestamp TEXT
    )
''')

def log_attendance(name):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO attendance (name, timestamp) VALUES (?, ?)", (name, timestamp))
    conn.commit()

# Recognize a single face
def recognize_face(image_path):
    img = cv2.imread(image_path)
    img_resized = cv2.resize(img, (128, 128)) / 255.0
    img_array = np.expand_dims(img_resized, axis=0)

    predictions = model.predict(img_array)
    label = np.argmax(predictions)
    accuracy = np.max(predictions) * 100  # Convert to percentage

    if accuracy > 90:  # Confidence threshold
        recognized_name = label_dict[label]
        print(f"Recognized: {recognized_name}, Accuracy: {accuracy:.2f}%")  # Display as percentage
        return recognized_name, accuracy
    else:
        print("Face not recognized or low accuracy.")  # Changed from confidence to accuracy
        return None, accuracy

# Test with an image
test_image = r"C:\Users\hp\Downloads\archive\lfw-deepfunneled\lfw-deepfunneled\lfw-deepfunneled\Gus_Van_Sant\Gus_Van_Sant_0001.jpg"
recognize_face(test_image)
