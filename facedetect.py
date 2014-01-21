#!/usr/bin/env python

import numpy as np
import cv2

# local modules
from video import create_capture
from common import clock, draw_str

help_message = '''
USAGE: facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=2, minSize=(10, 10), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

# Replace the draw_rects function with a process video.
def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__ == '__main__':
    import sys, getopt
    print help_message

    # Read in the arguments from terminal.
    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try:
        video_src = video_src[0]
    except:
        video_src = 0
    args = dict(args)
    # Load the classifiers.
    cascade_fn = args.get('--cascade', "cascades/haarcascade_frontalface_alt.xml")
    eye_fn  = args.get('--nested-cascade', "cascades/haarcascade_eye.xml")
    cascade = cv2.CascadeClassifier(cascade_fn)
    eye = cv2.CascadeClassifier(eye_fn)

    # Create the camera.
    cam = create_capture(video_src)
    # cam = cv2.CreateCamera

    # Create a queue.

    while True:
        # Reading in the image.
        success, img = cam.read()
        if (success):
            img = img[::5,::5].copy()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            gray = cv2.equalizeHist(gray)

            t = clock()
            rects = detect(gray, cascade)
            print rects
            vis = img.copy()
            draw_rects(vis, rects, (0, 255, 0))
            for x1, y1, x2, y2 in rects:
                roi = gray[y1:y2, x1:x2]
                vis_roi = vis[y1:y2, x1:x2]
                subrects = detect(roi.copy(), eye)
                draw_rects(vis_roi, subrects, (255, 0, 0))
            dt = clock() - t

            draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
            # Get the face.
            # vis[rects[0][1]:rects[0][3], rects[0][0]:rects[0][2]]
            # Add it to the queue.

            # If queue > some_size:
                # run the heartbeat code.
                # augment results onto vis.
                # cv2.imshow('facedetect', vis)
                # pop element from queue.
            cv2.imshow('facedetect', vis)
        else:
            break
        if 0xFF & cv2.waitKey(5) == 27:
            break
    cv2.destroyAllWindows()