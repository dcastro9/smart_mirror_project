#!/usr/bin/env python

import numpy as np
import cv2

# local modules
from video import create_capture
from common import clock, draw_str
from laplacian_pyramid import LaplacianPyramid

help_message = '''
USAGE: facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''
class Queue:
    size = 0
    def __init__(self):     # instantiates
        self.in_stack = []
        self.out_stack = []
        size = 0
    def push(self, obj):    # pushes object in
        self.in_stack.append(obj)
        size=self.size+1
    def pop(self):          # dequeus
        if self.size>0:
            size = self.size-1
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()
    def length(self):       # returns size
        return self.size
def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__ == '__main__':
    import sys, getopt
    print help_message

    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try:
        video_src = video_src[0]
    except:
        video_src = 0
    args = dict(args)
    cascade_fn = args.get('--cascade', "cascades/haarcascade_frontalface_alt.xml")
    nested_fn  = args.get('--nested-cascade', "cascades/haarcascade_eye.xml")

    cascade = cv2.CascadeClassifier(cascade_fn)
    nested = cv2.CascadeClassifier(nested_fn)

    cam = create_capture(video_src)
    q = Queue()
    frames = []
    while True:
        success, img = cam.read()
        if (success):
            img = img[::8,::8].copy()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.equalizeHist(gray)

            t = clock()
            rects = detect(gray, cascade)
            vis = img.copy()
            draw_rects(vis, rects, (0, 255, 0))
            for x1, y1, x2, y2 in rects:
                roi = gray[y1:y2, x1:x2]
                vis_roi = vis[y1:y2, x1:x2]
                subrects = detect(roi.copy(), nested)
                draw_rects(vis_roi, subrects, (255, 0, 0))
            dt = clock() - t

            draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
            cv2.imshow('facedetect', vis[y1:y2, x1:x2])
            q.push(vis[y1:y2, x1:x2])
            #if q.size >10:
             #   q.pop()
             #   img = img[::3,::3]
             #   frames.append(LaplacianPyramid(img, 2)._pyramid)
            #else:
             #   break
        else:
            break
        if 0xFF & cv2.waitKey(5) == 27:
            break
    cv2.destroyAllWindows()