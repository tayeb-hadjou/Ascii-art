import cv2
letter = ['@', '%', '#', '*', 'o','=','-',':',',','.']
pbs=1 #pixel block size
HEIGHT = 400
WIDTH = 400
class ImageToString:
    def __init__(self,frame):
        self.frame = frame 
    #gray scale 
    def get_gray_scale(self,frame):
        img = frame
        img = cv2.resize(img, (HEIGHT, WIDTH))
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
                text += letter[(int(avg)//26)]
            text += "\n"
        return text
    