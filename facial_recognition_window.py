import cv2
import face_recognition
from PyQt5.QtWidgets import QDialog, QPushButton
from PyQt5 import uic

class FacialRecognitionWindow(QDialog):
    def __init__(self):
        super(FacialRecognitionWindow, self).__init__()
        uic.loadUi('win7.ui', self)  # Relative path to the UI file

        # Button to start facial recognition
        self.recognition_button = self.findChild(QPushButton, "pushButton")
        self.recognition_button.clicked.connect(self.perform_facial_recognition)
        
        # Button to go back to the previous window
        self.back_button = self.findChild(QPushButton, "pushButton_2")
        self.back_button.clicked.connect(self.go_back)

    def go_back(self):
        self.table_window = TableWindow()  # Assuming you have a class named `TableWindow`
        self.table_window.show()
        self.close()

    def perform_facial_recognition(self):
        # Set up the database cursor
        cursor = con.cursor()

        # Fetch student photos from the database
        cursor.execute("SELECT photo FROM student")
        photo_records = cursor.fetchall()

        # Initialize the video capture
        video_capture = cv2.VideoCapture('MOVIE.mp4')  # Relative path to the video file
        
        # Prepare a list of known face encodings
        known_face_encodings = []
        for record in photo_records:
            for photo_filename in record:
                photo_path = f"studentpics/{photo_filename}.jpg"  # Assuming the image path is relative
                photo_image = cv2.imread(photo_path)
                rgb_image = cv2.cvtColor(photo_image, cv2.COLOR_BGR2RGB)
                face_locations = face_recognition.face_locations(rgb_image, model="hog")  # Use "hog" or "cnn"
                face_encodings = face_recognition.face_encodings(rgb_image, face_locations)
                if face_encodings:
                    known_face_encodings.append(face_encodings[0])

        # Perform facial recognition on the video
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            face_locations = face_recognition.face_locations(rgb_frame, model="hog")  # Use "hog" or "cnn"
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, encoding)
                if True in matches:
                    print("Access granted")
                else:
                    print("Access denied")

        video_capture.release()
        cv2.destroyAllWindows()
 