import sys
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QComboBox, QPushButton, QLineEdit, QFileDialog, QMessageBox
from util.its_class import ImageToString
import os
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt, QSize

class AppSetup(QDialog):    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Ascii Art")
        layout = self.setupQbox()
        self.setLayout(layout)
        self.setFont(QFont("Arial", 10))
        self.resize(400, 300)

        self.nbrLettre = 0
        self.framResize = (0, 0)
        self.data = {}

    def setupQbox(self):
        windowBox = QVBoxLayout()
        label1 = QLabel("Number of letter to use: ")
        label2 = QLabel("Frame resize: ")
        label3 = QLabel("Load a file: ")

        self.nbrInput = QComboBox()
        self.nbrInput.addItems(["5", "10", "92"])

        self.techniqueInput = QComboBox()
        self.techniqueInput.addItems(["400X400", "100X100", "40X40"])

        self.imagePathInput = QLineEdit()
        imageButton = QPushButton("Load Image/Video")
        imageButton.clicked.connect(self.loadImage)

        windowBox.addWidget(label1)
        windowBox.addWidget(self.nbrInput)
        windowBox.addWidget(label2)
        windowBox.addWidget(self.techniqueInput)
        windowBox.addWidget(label3)
        windowBox.addWidget(self.imagePathInput)
        windowBox.addWidget(imageButton)

        submitButton = QPushButton("Submit")
        windowBox.addWidget(submitButton)
        submitButton.clicked.connect(self.setData)

        return windowBox

    def loadImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp *.gif *.mp4);;All Files (*)", options=options)
        if file_path:
            self.imagePathInput.setText(file_path)
         

    def setData(self):
        if(self.techniqueInput.currentText() == "400X400"):
            fs= (400,400)
        elif(self.techniqueInput.currentText() == "100X100"):
            fs= (100,100)
        else:
            fs= (40,40)

        self.data = {
            
            "nbrL": int(self.nbrInput.currentText()),
            "fs": fs,
            "Image Path": self.imagePathInput.text()
        }
        
        self.accept()


    def getData(self):
        return self.data