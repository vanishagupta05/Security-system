from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QTableWidgetItem
from PyQt5 import uic, QtGui
import mysql.connector as mysql
import os

# Database connection
db_connection = mysql.connect(
    host='localhost',
    user='root',
    passwd='Vini2552',
    database='vanisha'
)
db_cursor = db_connection.cursor()

# Create necessary tables
db_cursor.execute('''CREATE TABLE IF NOT EXISTS student (
                        StudentID VARCHAR(10) PRIMARY KEY,
                        Name VARCHAR(20),
                        Phone BIGINT,
                        Photo VARCHAR(100),
                        Class VARCHAR(2),
                        HealthHistory VARCHAR(100)
                    )''')

db_cursor.execute('''CREATE TABLE IF NOT EXISTS teacher (
                        TeacherID VARCHAR(10) PRIMARY KEY,
                        Name VARCHAR(20),
                        Phone BIGINT,
                        Photo VARCHAR(100),
                        HealthHistory VARCHAR(100)
                    )''')

# Main Window for the application
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui_files/main_window.ui', self)
        
        # Connecting buttons to methods
        self.insert_btn = self.findChild(QPushButton, "pushButton_insert")
        self.insert_btn.clicked.connect(self.openInsertWindow)
        
        self.delete_btn = self.findChild(QPushButton, "pushButton_delete")
        self.delete_btn.clicked.connect(self.openDeleteWindow)
        
        self.modify_btn = self.findChild(QPushButton, "pushButton_modify")
        self.modify_btn.clicked.connect(self.openModifyWindow)
        
        self.search_btn = self.findChild(QPushButton, "pushButton_search")
        self.search_btn.clicked.connect(self.openSearchWindow)
        
        self.display_btn = self.findChild(QPushButton, "pushButton_display")
        self.display_btn.clicked.connect(self.openDisplayWindow)

        self.facial_btn = self.findChild(QPushButton, "pushButton_facial")
        self.facial_btn.clicked.connect(self.openFacialRecognitionWindow)
        
        self.back_btn = self.findChild(QPushButton, "pushButton_back")
        self.back_btn.clicked.connect(self.goBack)
        
    # Define methods for opening new windows
    def openInsertWindow(self):
        self.insert_window = InsertWindow()
        self.insert_window.show()

    def openDeleteWindow(self):
        self.delete_window = DeleteWindow()
        self.delete_window.show()

    def openModifyWindow(self):
        self.modify_window = ModifyWindow()
        self.modify_window.show()

    def openSearchWindow(self):
        self.search_window = SearchWindow()
        self.search_window.show()

    def openDisplayWindow(self):
        self.display_window = DisplayWindow()
        self.display_window.show()

    def openFacialRecognitionWindow(self):
        self.facial_window = FacialRecognitionWindow()
        self.facial_window.show()

    def goBack(self):
        self.close()
