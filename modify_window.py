from PyQt5.QtWidgets import QDialog, QPushButton
from PyQt5 import uic
import MySQLdb  # Assuming you're using MySQL, replace with your actual DB library

class ModifyRecords(QDialog):
    def __init__(self):
        super(ModifyRecords, self).__init__()
        # Load the UI file with a relative path
        uic.loadUi('win4.ui', self)

        # Find buttons and connect them to their respective functions
        self.updateButton = self.findChild(QPushButton, "pushButton")
        self.updateButton.clicked.connect(self.modify_record)

        self.backButton = self.findChild(QPushButton, "pushButton_2")
        self.backButton.clicked.connect(self.go_back)

    def go_back(self):  # Navigate back to the table window
        self.tableWindow = TableWindow()  # Assuming you have a class named `TableWindow`
        self.tableWindow.show()
        self.close()

    def modify_record(self):
        student_id = self.lineEdit.text()
        column_to_modify = self.comboBox.currentText()
        new_value = self.lineEdit_2.text()

        if column_to_modify == 'name':
            cur.execute('UPDATE student SET name = %s WHERE StudentID = %s', (new_value, student_id))
        elif column_to_modify == 'phone-no':
            cur.execute('UPDATE student SET phone = %s WHERE StudentID = %s', (new_value, student_id))
        elif column_to_modify == 'pic':
            cur.execute('UPDATE student SET photo = %s WHERE StudentID = %s', (new_value, student_id))
        elif column_to_modify == 'H-History':
            cur.execute('UPDATE student SET health = %s WHERE StudentID = %s', (new_value, student_id))
        elif column_to_modify == 'class':
            cur.execute('UPDATE student SET Class = %s WHERE StudentID = %s', (new_value, student_id))

        con.commit()  # Commit the transaction to the database

        # Set a label to confirm the update
        self.label_3.setText("Records have been updated")

