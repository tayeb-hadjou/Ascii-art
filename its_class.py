import cv2
from util import PBS,COMBINATION,RESIZE_WEBCAM

NBR_LETTER=5
pbs=PBS
resize = RESIZE_WEBCAM
letter=COMBINATION["letter_"+str(NBR_LETTER)]["letter"]
div=COMBINATION["letter_"+str(NBR_LETTER)]["div"]

class ImageToString:
    def __init__(self,frame):
        self.frame = frame 
    #gray scale 
    def get_gray_scale(self,frame):
        img = frame
        img = cv2.resize(img, resize)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return img_gray

    def image_to_string(self):
        text = ""
        img_gray = self.get_gray_scale(self.frame)
        img_height = img_gray.shape[0]
        img_width = img_gray.shape[1]
        for i in range(0,img_height,pbs):
            for j in range(0,img_width,pbs):
                avg = img_gray[i:i+pbs,j:j+pbs].mean()
                text += letter[(int(avg)//div)]
            text += "\n"
        return text
    