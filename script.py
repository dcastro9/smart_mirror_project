import scipy
import numpy
import cv2

video = cv2.VideoCapture("sample.mp4")
frames = []
i = 0
#reading in the video
while(True):
    success, img = video.read()
    if success:
        frames.append(img)
    else:
        break