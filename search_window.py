from PyQt5.QtWidgets import QDialog, QPushButton, QTableWidgetItem
from PyQt5 import uic, QtGui
import MySQLdb  # Assuming you're using MySQL, replace with your actual DB library

class SearchWindow(QDialog):
    def __init__(self):
        super(SearchWindow, self).__init__()
        uic.loadUi('win5.ui', self)  # Relative path to the UI file
        
        # Button connections
        self.studentInfoButton = self.findChild(QPushButton, "pushButton")
        self.studentInfoButton.clicked.connect(self.show_student_info)
        
        self.anotherActionButton = self.findChild(QPushButton, "pushButton_3")
        self.anotherActionButton.clicked.connect(self.show_another_action)
        
        self.backButton = self.findChild(QPushButton, "pushButton_4")
        self.backButton.clicked.connect(self.go_back)
    
    def go_back(self):
        self.tableWindow = MainWindow()  # Assuming you have a class named `TableWindow`
        self.tableWindow.show()
        self.close()
    
    def show_student_info(self):
        self.studentInfoWindow = StudentInfoDialog()
        self.studentInfoWindow.show()
        print("Student Info Window opened")
    
    def show_another_action(self):
        self.anotherActionWindow = AnotherActionDialog()
        self.anotherActionWindow.show()
        print("Another Action Window opened")


class StudentInfoDialog(QDialog):
    def __init__(self):
        super(StudentInfoDialog, self).__init__()
        uic.loadUi('studentpic/win5a.ui', self)  # Relative path to the UI file

        # Button connections
        self.searchButton = self.findChild(QPushButton, "pushButton")
        self.searchButton.clicked.connect(self.search_student_by_id)
        
        self.backButton = self.findChild(QPushButton, "pushButton_2")
        self.backButton.clicked.connect(self.go_back)
    
    def go_back(self):
        self.tableWindow = TableWindow()
        self.tableWindow.show()
        self.close()

    # Function to search student by ID and display information
    def search_student_by_id(self):
        student_id = self.lineEdit.text()
        print(f"Searching for student with ID: {student_id}")
        
        cur.execute("SELECT * FROM student WHERE StudentID = %s", (student_id,))
        student_data = cur.fetchall()

        if student_data:
            self.label_3.setText(student_data[0][1])  # Assuming label_3 is for displaying student name
            self.label_10.setText(student_data[0][4])  # Assuming label_10 is for some other info
            self.label_11.setText(student_data[0][5])  # Assuming label_11 is for some other info
            self.label_12.setText(str(student_data[0][2]))  # Displaying some integer or numeric value

            # Construct image path dynamically
            image_path = f"studentpics/{student_data[0][3]}.jpg"  # Assuming the image is stored with StudentID.jpg
            self.label_8.setPixmap(QtGui.QPixmap(image_path))
            self.show()
        else:
            print("No data found")


class EntireTableActionDialog(QDialog):
    def __init__(self):
        super(TeacherActionDialog, self).__init__()
        uic.loadUi('win5b.ui', self)  # Relative path to the UI file
        print("Another Action Dialog initialized")

        # Button connections
        self.searchButton = self.findChild(QPushButton, "pushButton_2")
        self.searchButton.clicked.connect(self.search_by_class)
        
        self.backButton = self.findChild(QPushButton, "pushButton")
        self.backButton.clicked.connect(self.go_back)
    
    def go_back(self):
        self.tableWindow = TableWindow()
        self.tableWindow.show()
        self.close()

    # Function to search students by class and populate the table
    def search_by_class(self):
        class_name = self.lineEdit.text()
        cur.execute("SELECT * FROM student WHERE Class = %s", (class_name,))
        students = cur.fetchall()

        row = 0
        self.tableWidget.setRowCount(len(students))
        for student in students:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(student[0])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(student[1]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(student[2])))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(student[3]))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(student[4]))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(student[5]))
            row += 1
