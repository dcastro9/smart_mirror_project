import scipy
import numpy
import cv2

video = cv2.VideoCapture("monstertruck.flv")
cv2.namedWindow("Test Video")
while(True):
    success, img = video.read()
    if success:
        cv2.imshow("Test Video", img)
        cv2.waitKey(50) # Changes to this alter the frame rate.
    else:
        break