# Automatic Attendance System Using Machine Learning

This project uses **machine learning** and **facial recognition** to automate the attendance management process. It leverages **Convolutional Neural Networks (CNNs)** for face detection and recognition to track and log attendance accurately in real-time. The system aims to reduce human intervention, minimize errors, and increase efficiency in attendance management.

## Features
- **Facial Recognition**: Improved accuracy threshold for face recognition.
- **Automated Attendance**: Real-time logging of attendance with minimal human intervention.
- **User Interface**: The GUI allows users to upload images for recognition, log attendance, and view attendance records.
- **Database Integration**: SQLite-based database to store attendance records.


## Technologies Used
- **Python** (3.x)
- **TensorFlow** / **Keras** for machine learning model
- **OpenCV** for image processing
- **SQLite3** for database management
- **NumPy** and **Pandas** for data manipulation

## Prerequisites

Before running this project, ensure you have the following installed:

- **Python 3.7+**
- **TensorFlow**: for building and training the machine learning model.
  ```bash
  pip install tensorflow
  ```
- **OpenCV**: for image capture and preprocessing.
  ```bash
  pip install opencv-python
  ```
- **SQLite3**: for managing the attendance database (usually pre-installed with Python).
  ```bash
  pip install sqlite3
  ```

## Project Structure

```
automatic-attendance-system/
│
├── dataset/               # Folder to store images of individuals for training
├── app.py                 # Main script to run the app and start attendance logging
├── train.py               # Python script to train the model
├── recognize.py           # Python script to recognize faces and log attendance
├── preprocess.py          # Preprocessing of images and labels
├── attendance.db          # SQLite database for attendance (auto-created)
└── README.md              # Project documentation
```

## How to Run

### 1. **Prepare the Dataset**:
- Create a folder `dataset/` and place images of individuals in it.
- Each folder within `dataset/` should be named after the person and contain multiple images of them.

### 2. **Using the GUI**:
- Run the application using the command `python attendance_gui.py`.
- Use the "Upload Image" button to select an image for recognition.
- Click "Recognize" to identify the person in the uploaded image.
- If recognized, click "Log Attendance" to record the attendance.
- Use the "Display Attendance Records" button to view logged attendance.


### 2. **Train the Model**:
Run the following command to train the facial recognition model:
```bash
python train.py
```
This will train the model on the images in the `dataset/` folder and save the trained model as `face_recognition_model.h5`.

### 3. **Run Attendance Recognition**:
Once the model is trained, you can use the following command to start recognizing faces and log attendance in real-time:
```bash
python recognize.py
```
This will capture images from your webcam, recognize faces, and log the attendance in an SQLite database.

## Database

The attendance records are stored in an SQLite database. The system tracks attendance by comparing the recognized faces with the labels stored in the database. Attendance is logged with timestamps for each recognized individual.

## Model Details

The model used in this project is a Convolutional Neural Network (CNN) trained to recognize faces. The architecture of the model consists of:
- **Convolutional layers** for feature extraction.
- **MaxPooling layers** for down-sampling.
- **Fully connected layers** to classify individuals.

## Expected Outcomes
- **Reduced manual effort** in attendance management.
- **Increased accuracy** in attendance tracking.
- **Time-saving** through automation.
- **Real-time attendance monitoring** and reporting.

---

Feel free to contribute to this project or make modifications based on your requirements.
