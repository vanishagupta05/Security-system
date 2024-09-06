# Facial Recognition System for Student Safety
![Security system] ](Picture1.jpg)
## Project Overview

The Facial Recognition System is designed to enhance security and safety in educational institutions by leveraging face recognition technology. The system maps facial features mathematically and compares them against a database to verify an individual’s identity. The goal is to create a secure and user-friendly solution to monitor and ensure the safety of students and staff within the premises.

## Purpose

The project aims to utilize facial recognition technology to build software that helps improve the safety and security of students. By integrating Python and machine learning, the system uses facial recognition and SQL to manage and verify student and staff information. It compares live or digital images with stored faceprints in the database, issuing alerts if no match is found, and granting access if a match is confirmed. This technology is particularly valuable in ensuring safety in sensitive areas, such as restrooms, where incidents have raised concerns.

## System Requirements

- **Minimum RAM Size**: 4 MB
- **Minimum Hard Drive Size**: 25 MB
- **OS Required**: Windows (64 Bit)
- **Minimum Processor Type**: Intel 386 or higher
- **Platform**: Any Python Editor (IDLE 3.10.8)
- **Programming Language**: Python
- **Database**: SQL

## Project Design

## Flowchart
![Workflow of all the windows ](Flowchart.png)

### Inbuilt Functions Used

- **Imutils**: `paths`, `face_recognition`, `argparse`, `cv2`
- **PyQt5**: `QtWidgets`, `uic`, `QtGui`, `QtCore`, `base64`
- **PyQt5Widgets**: `QApplication`, `QWidget`, `QMainWindow`, `QDialog`, `QPushButton`, `QComboBox`, `QTableWidgetItem`
- **mysql.connector**: `Connect()`, `commit()`, `cursor()`
- **PIL**: `Image`, `io`
- **OS**: `system(cls)`

### User-Defined Functions

- **`Index`**: Displays the student table menu.
- **`Index2`**: Displays the staff table menu.
- **`Win`**: Navigates back to the main menu.
- **`InsertWindow()`**: Inserts records into the student table.
- **`DeleteWindow()`**: Deletes records from the student table.
- **`ModifyWindow()`**: Modifies records in the student table.
- **`SearchWindow()`**: Searches records in the student table.
- **``**: Searches student information by ID.
- **`StudentInfoDialog()`**: Searches student records by class.
- **`DisplyWindow()`**: Displays the complete student table.
- **`FacialWindow()`**: Performs facial recognition to verify individuals.
## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/facial-recognition-system.git
2. **Required Packages**:
'''pip install PyQt5 mysql-connector-python pillow opencv-python imutils face_recognition

## Outputs


![Entering username](output1.png)
![user/staff][output2.png]
![Index][/Users/vanishagupta/Projects/security-system/output3.jpg]
![InsertWindow][output4.jpg]
![DeleteWindow][out6.jpg]
![ModifyWindow][output7.jpg]
![SeatchWindow][output9.png]
![StudentInfoDialog][output10.png]
![StudentInfoDialog2][output11.png]
![DisplayWindow][output13.png]
![FacialWindow][output17.png]
