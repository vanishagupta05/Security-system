# delete_window.py
from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QLabel
from PyQt5 import uic
from db_connection import cursor, connection

class DeleteWindow(QDialog):
    def __init__(self):
        super(DeleteWindow, self).__init__()
        uic.loadUi(r'..\project\delete_window.ui', self)

        # Button and input fields
        self.delete_button = self.findChild(QPushButton, "pushButton")
        self.delete_button.clicked.connect(self.delete_record)

        self.back_button = self.findChild(QPushButton, "pushButton_2")
        self.back_button.clicked.connect(self.go_back)

        self.student_id_input = self.findChild(QLineEdit, "lineEdit")
        self.message_label = self.findChild(QLabel, "label_3")

    def delete_record(self):
        student_id = self.student_id_input.text()

        cursor.execute("SELECT * FROM student WHERE StudentID = %s", (student_id,))
        record = cursor.fetchone()

        if record:
            cursor.execute("DELETE FROM student WHERE StudentID = %s", (student_id,))
            connection.commit()
            self.message_label.setText("Record deleted successfully")
        else:
            self.message_label.setText("No such record found")

    def go_back(self):
        self.close()
