import scipy
import numpy
import cv2

video = cv2.VideoCapture("horse.avi")
cv2.namedWindow("Test Video")
while(True):
    f, img = video.read()
    if img != None:
        cv2.imshow("Test Video", img)
        cv2.waitKey(200) # Changes to this alter the frame rate.
    else:
        break