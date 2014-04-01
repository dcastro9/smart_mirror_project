import cv2

# local modules
from video import create_capture
from common import clock, draw_str

class FaceDetector(object):
    def __init__(self, cascade_fn, nested_fn=None):
        self.cascade = cv2.CascadeClassifier(cascade_fn)
        if (None != nested_fn):
            self.nested = cv2.CascadeClassifier(nested_fn)

    def detect(img):
        rects = self.cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
        if len(rects) == 0:
            return []
        rects[:,2:] += rects[:,:2]
        return rects

    def draw_rects(img, rects, color):
        for x1, y1, x2, y2 in rects:
            cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)