import cv2
from util.options import COMBINATION


class ImageToString:
    def __init__(self,frame,params):
        self.frame = frame 
        self.resize = params["fs"]
        self.letter = COMBINATION["letter_"+str(params["nbrL"])]["letter"]
        self.div = COMBINATION["letter_"+str(params["nbrL"])]["div"]
        self.pbs = 1 
    def get_gray_scale(self,frame):
        img = frame
        img = cv2.resize(img, self.resize)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return img_gray

    def image_to_string(self):
        text = ""
        img_gray = self.get_gray_scale(self.frame)
        img_height = img_gray.shape[0]
        img_width = img_gray.shape[1]
        for i in range(0,img_height,self.pbs):
            for j in range(0,img_width,self.pbs):
                avg = img_gray[i:i+self.pbs,j:j+self.pbs].mean()
                text += self.letter[(int(avg)//self.div)]
            text += "\n"
        return text    