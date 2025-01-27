from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense # type: ignore
from tensorflow.keras.utils import to_categorical # type: ignore
from sklearn.model_selection import train_test_split
import numpy as np
from preprocess import preprocess_images

# Load and preprocess data
data_dir = r"C:\Users\hp\Downloads\archive\lfw-deepfunneled\lfw-deepfunneled\lfw-deepfunneled"
images, labels, label_dict = preprocess_images(data_dir)

# Check the number of unique classes
print(f"Unique classes: {len(set(labels))}")  

# Split data
X_train, X_test, y_train, y_test = train_test_split(images, labels, test_size=0.2, random_state=42)

# One-hot encode labels
y_train_one_hot = to_categorical(y_train,num_classes=len(set(labels)))
y_test_one_hot = to_categorical(y_test,num_classes=len(set(labels)))

# Build the model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(128, 128, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(2150, activation='softmax')  
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train_one_hot, validation_data=(X_test, y_test_one_hot), epochs=20, batch_size=16)  

# Save the model
model.save("face_recognition_model.h5")
print("Model saved as face_recognition_model.h5")
