from eulerian_video_magnification import EulerianVideoMagnification
import numpy as np
from cv2 import VideoCapture

frames = []
video = VideoCapture("sample.mp4")
for val in range(90):
	success, img = video.read()
	if success:
		frames.append(img[::2,::2])
	else:
		break

evm = EulerianVideoMagnification(frames, levels=3)
evm.run()
