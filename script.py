#from webcam_heartbeat_monitor import WebcamHeartbeatMonitor

#whm = WebcamHeartbeatMonitor(30*10)
#whm.run()

from eulerian_video_magnification import EulerianVideoMagnification
import numpy as np
import cv2

frames = []
video = cv2.VideoCapture("sample.mp4")
for val in range(180):
	success, img = video.read()
	if success:
		frames.append(img[::2,::2])
	else:
		break

#evm = EulerianVideoMagnification(frames, levels=3)
#result = evm.process()
whm = WebcamHeartbeatMonitor(30*10)
whm.run()
win = cv2.namedWindow("Image Capture")

for frame in result:
	cv2.imshow("Image Capture", frame)
	cv2.waitKey(20)
