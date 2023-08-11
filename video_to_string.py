from its_class import ImageToString
import cv2 

def video_to_string(video_path):
    cap=cv2.VideoCapture(video_path)
    while cap.isOpened():
        ret,frame=cap.read()
        if ret:
            img_to_string=ImageToString(frame).image_to_string()
            print(img_to_string)
        else:
            break

if __name__ == '__main__':
    video_path='video.mp4'
    video_to_string(video_path)