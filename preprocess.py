import cv2
import numpy as np
import os
data_dir=r"C:\Users\hp\Downloads\archive\lfw-deepfunneled\lfw-deepfunneled\lfw-deepfunneled"
def preprocess_images(data_dir, img_size=(128, 128)):
    images = []
    labels = []
    label_dict = {}

    for label, person_name in enumerate(os.listdir(data_dir)):
        person_dir = os.path.join(data_dir, person_name)
        if os.path.isdir(person_dir):
            label_dict[label] = person_name
            for image_name in os.listdir(person_dir):
                image_path = os.path.join(person_dir, image_name)
                img = cv2.imread(image_path)
                if img is not None:
                    img = cv2.resize(img, img_size)  # Resize to 128x128
                    images.append(img / 255.0)      # Normalize pixels
                    labels.append(label)
        for label, person_name in enumerate(os.listdir(data_dir)):
            person_dir = os.path.join(data_dir, person_name)
        if os.path.isdir(person_dir):
            label_dict[label] = person_name

    return np.array(images), np.array(labels), label_dict




