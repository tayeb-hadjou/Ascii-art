from PyQt5.QtWidgets import *
from its_class import *
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QFont

class AppSetup(QDialog):
    title = "Setup"
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle(self.title)
        layout = self.setupQbox()
        self.setLayout(layout)
        self.nbrLettre = 0
        self.framResize = (0, 0)
        self.data = {}

    def setupQbox(self):
        windowBox = QVBoxLayout()
        label1 = QLabel("Number of letter to use: ")
        label2 = QLabel("Frame resize: ")
        label3 = QLabel("Load an image: ")

        self.nbrInput = QComboBox()
        self.nbrInput.addItems(["5", "10", "92"])

        self.techniqueInput = QComboBox()
        self.techniqueInput.addItems(["Image", "Video", "Webcam"])

        self.imagePathInput = QLineEdit()
        imageButton = QPushButton("Load Image")
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
        filePath, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp *.gif);;All Files (*)", options=options)
        if filePath:
            self.imagePathInput.setText(filePath)
         

    def setData(self):
        if(self.techniqueInput.currentText() == "Image"):
            fs= (400,400)
        elif(self.techniqueInput.currentText() == "Video"):
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

def display_result(data):
    img = cv2.imread(data["Image Path"])
    text = ImageToString(img,data).image_to_string()
    #display text in a window
    window = QWidget()
    window.setWindowTitle("Text")
    window.resize(500, 500)
    
    layout = QVBoxLayout()
    label = QLabel(text)
    label.setFont(QFont('Arial', 2))
    #zoom out 
    #label.setFont(QFont('Arial', 2))
    layout.addWidget(label)
    window.setLayout(layout)
    
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication([])
    setup = AppSetup()
    
    if setup.exec_() == QDialog.Accepted:
        data = setup.getData()
        display_result(data)
    app.exec_()

