import sys
import pyperclip
from PyQt5.QtWidgets import *
from util.its_class import ImageToString
import os
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt, QSize
import cv2
from widgets.Choice import AppChoice
from widgets.AppSetup import AppSetup
from util.webcam_to_string import webcam_to_string
from util.video_to_string import video_to_string

def copy_result(data):
    img = cv2.imread(data["Image Path"])
    text = ImageToString(img,data).image_to_string()
    pyperclip.copy(text)
    msg = QMessageBox()
    msg.setWindowTitle("Text Copied!")
    msg.setText("The text has been copied")
    msg.setIcon(QMessageBox.Information)
    msg.setStandardButtons(QMessageBox.Ok)
    sys.exit(msg.exec_())

def main():
    app = QApplication([])
    choice = AppChoice()
    if choice.exec_() == QDialog.Accepted :
        if choice.choice == "Image":
            setup = AppSetup()
            if setup.exec_() == QDialog.Accepted :
                data = setup.getData()
                copy_result(data)
        elif choice.choice == "Webcam":
            webcam_to_string()
        else:
            setup = AppSetup()
            if setup.exec_() == QDialog.Accepted :
                data = setup.getData()
                video_to_string(data["Image Path"],data)
    app.quit()
if __name__ == '__main__':
    main()