import numpy as np

from cv2 import VideoCapture
from eulerian_video_magnification import EulerianVideoMagnification
from scipy.signal import butter
from scipy.signal import lfilter

class Queue(object):
    """Implementation of a queue.
    """
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, obj):
        self.in_stack.append(obj)

    def pop(self):
        # TODO: Figure out what happens when pop is empty.
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
        self._eulerian_video_magnification = EulerianVideoMagnification()
        self._num_frames = num_frames 

        if self._video_capture.isOpened():
            rval, frame = vc.read()
        else:
            rval = False

    def run(self):
        while rval:
            rval, frame = vc.read()
            # Run the face detector on the frame.
            face_image = self._face_detector.process(frame)

            self._img_queue.push(face_image)
            if self._img_queue.length() > self._num_frames:
                self._img_queue.pop()
                # TODO(dcastro): Rewrite EVM to process frames.
                frames = self._eulerian_video_magnification.process(
                        self._img_queue.current_queue(self._num_frames))
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

    def process(img):
        """Processes any given image and returns the first face it finds.

        Returns:
           A cropped image of the face.
        """
        # TODO(vjain): Think about alternate ways of getting the face
        # (consistent).
        rects = self.__detect(img)
        for x1, y1, x2, y2 in rects:
            # TODO(vjain): Resize the imge to dimension.
            return img[y1:y2, x1:x2]