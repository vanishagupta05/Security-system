import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton
from PyQt5 import uic

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('win.ui', self)  # Relative path to the UI file

        # Button for student section
        self.student_button = self.findChild(QPushButton, "pushButton")
        self.student_button.clicked.connect(self.open_student_window)

        # Button for staff section
        self.staff_button = self.findChild(QPushButton, "pushButton_2")
        self.staff_button.clicked.connect(self.open_staff_window)

    def open_student_window(self):
        self.student_window = StudentWindow()  # Assuming you have a class named `StudentWindow`
        self.student_window.show()

    def open_staff_window(self):
        self.staff_window = StaffWindow()  # Assuming you have a class named `StaffWindow`
        self.staff_window.show()


class LoginWindow(QDialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        uic.loadUi('login.ui', self)  # Relative path to the UI file

        # Button to login
        self.login_button = self.findChild(QPushButton, "pushButton")
        self.login_button.clicked.connect(self.authenticate)

    def authenticate(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if username == 'A' and password == '1':
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()  # Close the login window
        else:
            self.label_3.setText("Incorrect username or password")


# Main section
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
