from its_class import ImageToString
import cv2 

def webcam_to_string():
    cap=cv2.VideoCapture(0)
    #show caption

    cap.set(3,48)
    while True:
        ret,frame=cap.read()
        img_to_string=ImageToString(frame).image_to_string()
        #use terminal to see the output
        print(img_to_string)
        #clear the terminal
        #print(chr(27) + "[2J")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()


if __name__ == '__main__':
    webcam_to_string()