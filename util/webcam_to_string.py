from util.its_class import ImageToString
import cv2 

def webcam_to_string():
    cap=cv2.VideoCapture(0)
    params={
            
            "nbrL": 5,
            "fs": (50,50),        
    }

    cap.set(3,48)
    while True:
        _,frame=cap.read()
        img_to_string=ImageToString(frame,params).image_to_string()
        print(img_to_string)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()


if __name__ == '__main__':
    webcam_to_string()