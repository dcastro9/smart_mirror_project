from eulerian_video_magnification import EulerianVideoMagnification
from webcam_heartbeat_monitor import WebcamHeartbeatMonitor
import numpy as np
import cv2
	
whm = WebcamHeartbeatMonitor(30*10)
whm.debug()
#win = cv2.namedWindow("Image Capture")
#cv2.waitKey(10000)
