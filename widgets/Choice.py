import sys
import pyperclip
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton, QLineEdit, QFileDialog, QMessageBox
from util.its_class import ImageToString
import os
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt, QSize


class AppChoice(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Ascii Art")
        layout = self.setupQbox()
        self.setFont(QFont("Arial", 10))
        self.resize(400, 100)
        self.setLayout(layout)
        self.show()

    def setupQbox(self):
        windowBox = QVBoxLayout()
        label1 = QLabel("Choose an option: ")
        self.c = QComboBox()
        self.c.addItems(["Image", "Video", "Webcam"])
        windowBox.addWidget(label1)
        windowBox.addWidget(self.c)
        submitButton = QPushButton("Submit")
        windowBox.addWidget(submitButton)
        submitButton.clicked.connect(self.setData)
        
        return windowBox
        
    def setData(self):
        if(self.c.currentText() == "Image"):
            self.choice = "Image"
            self.accept()
        elif (self.c.currentText() == "Video"):
            self.choice = "Video"
            self.accept()
        else:
            self.choice = "Webcam"
            self.accept()