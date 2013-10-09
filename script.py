import scipy
import numpy
import cv2

video = cv2.VideoCapture("sample.mp4")
frames = []
i = 0
# This is a loop.
while(True):
    success, img = video.read()
    if success:
        frames.append(img)
    else:
        break