# Copyright 2014, All Rights Reserved
# Author: Vikram Jain <vjain40@gatech.edu>
# Author: Daniel Castro <dcastro9@gatech.edu>

import numpy as np
import Image
import cv2
from eulerian_video_magnification import EulerianVideoMagnification
from scipy.signal import butter
from scipy.signal import lfilter

class Queue(object):
    """Implementation of a queue.
    """

    def __init__(self):
        self.in_stack = []
        self.out_stack = []
        self._size = 0

    def push(self, obj):
        self.in_stack.append(obj)
        self._size += 1

    def pop(self):
        # TODO: Figure out what happens when pop is empty. -- returns nothing 
	if self._size == 0:
		return
	else:
		self._size -= 1
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def length(self):
        return len(self.in_stack + self.out_stack)

    def current_queue(self, size):
        return (self.out_stack + self.in_stack)[:size]

class WebcamHeartbeatMonitor(object):
    """Performs Eulerian Video Magnification on a Webcam feed.
    """

    def __init__(self, num_frames):
        """Sets up the video magnification and webcam feed.
        """
        self._video_capture = cv2.VideoCapture(0)
        self._window = cv2.namedWindow("Image Capture")
        self._hb_monitor = cv2.namedWindow("Heartbeat")
        self._img_queue = Queue()
        self._hb_queue = Queue()
        self._face_detector = FaceDetector((50,50))
        self._num_frames = num_frames 

        if self._video_capture.isOpened():
            self._rval, frame = self._video_capture.read()
        else:
            self._rval = False
    def debug(self): #for debugging purposes
	frames = []
	for val in range(180):
		success, img = self._video_capture.read()
		face_image = self._face_detector.process(img)
		cv2.imshow("asd", face_image)
		if success:
			frames.append(face_image[::2,::2])
		else:
			break
		cv2.waitKey(20)
	#tmp.destory
	evm = EulerianVideoMagnification(frames, levels=3)
	result = evm.process()
	win = cv2.namedWindow("Image Capture")
	for frame in result:
		cv2.imshow("Image Capture", frame)
		cv2.waitKey(20)
    def run2(self):		# to debug
	 while self._rval:
            self._rval, frame = self._video_capture.read()
            # Run the face detector on the frame.
            face_image = self._face_detector.process(frame)
	    cv2.imshow("Image Capture", face_image)
	    cv2.waitKey(20)
            self._img_queue.push(face_image)
            if self._img_queue.length() > self._num_frames:
                self._img_queue.pop()
                evm = EulerianVideoMagnification(
                    self._img_queue.current_queue(self._num_frames), levels=3)
                frames = evm.process()
                if self._hb_queue.length() == 0:
                    for frame in frames:
                        self._hb_queue.push(frame)
                else:
                    self._hb_queue.push(frames[len(frames) - 1])
            if self._hb_queue.length() > 0:
                cv2.imshow("Heartbeat", self._hb_queue.pop())
		print("asd")

            key = cv2.waitKey(20)
            if key == 27: # Escape key.
                break
    def run(self):
        while self._rval:
            self._rval, frame = self._video_capture.read()
            # Run the face detector on the frame.
            face_image = self._face_detector.process(frame)
            self._img_queue.push(face_image)
            if self._img_queue.length() > self._num_frames:
                self._img_queue.pop()
                evm = EulerianVideoMagnification(
                    self._img_queue.current_queue(self._num_frames))
                frames = evm.process()
                if self._hb_queue.length() == 0:
                    for frame in frames:
                        self._hb_queue.push(frame)
                else:
                    self._hb_queue.push(frames[frames.length - 1])

            cv2.imshow("Image Capture", frame)

            if self._hb_queue.length() > 0:
                cv2.imshow("Heartbeat", self._hb_queue.pop())

            key = cv2.waitKey(20)
            if key == 27: # Escape key.
                break

    def shutdown(self):
        cv2.destroyWindow("Image Capture")
        cv2.destroyWindow("Heartbeat")


class FaceDetector(object):
    """ Processes an image and returns the cropped face for a given length
    and width. Returned image will be cropped to that size.

    Attributes:
       dimension: Tuple of length 2, contains the length & width of desired
                  face size.
    """

    def __init__(self, dimension,
                 cascade_fn="cascades/haarcascade_frontalface_alt.xml",
                 nested_fn="cascades/haarcascade_eye.xml"):
        """Creates a class to detect faces in an image.
        """
        self._dimension = dimension
        self._cascade = cv2.CascadeClassifier(cascade_fn)
        self._nested = cv2.CascadeClassifier(nested_fn)

    def __detect(self, img):
        """Private method to process the classifiers on an image.
        """
        rects = self._cascade.detectMultiScale(img,
                                               scaleFactor=1.3,
                                               minNeighbors=4,
                                               minSize=(30, 30),
                                               flags = cv2.CASCADE_SCALE_IMAGE)
        if len(rects) == 0:
            return []
        rects[:,2:] += rects[:,:2]
        return rects

    def process(self, img):
        """Processes any given image and returns the first face it finds.

        Returns:
           A cropped image of the face.
        """
        # TODO(vjain): Think about alternate ways of getting the face
        # (consistent). extrapolation using the PIL library? focusing on certan part of image
	    # suppose dim = l, w (length, width)

        rects = self.__detect(img)
	for x1, y1, x2, y2 in rects:
		if ((round((y2-y1)/(self._dimension[0])))>0 and int(round((x2-x1)/(self._dimension[1])))>0):
	  		img = img[y1:y2:int(round((y2-y1)/(self._dimension[0]))),
				x1:x2:int(round((x2-x1)/(self._dimension[1])))]
	
		#return new_im
        return img
