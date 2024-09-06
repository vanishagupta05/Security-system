# insert_window.py
from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QLabel
from PyQt5 import uic
from db_connection import cursor, connection

class InsertWindow(QDialog):
    def __init__(self):
        super(InsertWindow, self).__init__()
        uic.loadUi(r'Project\insert_window.ui', self)

        # Button and input fields
        self.insert_button = self.findChild(QPushButton, "pushButton")
        self.insert_button.clicked.connect(self.insert_record)

        self.back_button = self.findChild(QPushButton, "pushButton_2")
        self.back_button.clicked.connect(self.go_back)

        self.student_id_input = self.findChild(QLineEdit, "lineEdit")
        self.name_input = self.findChild(QLineEdit, "lineEdit_2")
        self.photo_input = self.findChild(QLineEdit, "lineEdit_3")
        self.phone_input = self.findChild(QLineEdit, "lineEdit_4")
        self.health_input = self.findChild(QLineEdit, "lineEdit_5")
        self.class_input = self.findChild(QLineEdit, "lineEdit_6")

        self.message_label = self.findChild(QLabel, "label_8")

    def insert_record(self):
        student_id = self.student_id_input.text()
        name = self.name_input.text()
        photo = self.photo_input.text()
        phone = self.phone_input.text()
        health_history = self.health_input.text()
        class_ = self.class_input.text()

        if not all([student_id, name, photo, phone, health_history, class_]):
            self.message_label.setText("Please input all the data")
        else:
            try:
                cursor.execute(f"""
                    INSERT INTO student (StudentID, Name, Phone, Photo, Class, HealthHistory) 
                    VALUES ('{student_id}', '{name}', {int(phone)}, '{photo}', '{class_}', '{health_history}')
                """)
                connection.commit()
                self.message_label.setText("Record inserted successfully")
            except Exception as e:
                self.message_label.setText(f"Error: {e}")

    def go_back(self):
        self.close()
