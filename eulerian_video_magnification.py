import numpy

from cv2 import VideoCapture

class EulerianVideoMagnification(object):
    """Provides a wrapper for Eulerian Video Magnification processing.

    Example:
        evm = EulerianVideoMagnification("path/to/video/file")
        evm.run()
    
    Attributes:
       video_path: The location of the video you wish to process.
    """

    def __init__(self, video_path):
        """Initializes the video magnification process by obtaining the frames.
        """
        self._video_path = video_path
        self._frames = []

        # Split into frames
        video = VideoCapture(video_path)
        while True:
            success, img = video.read()
            if success:
                # Add to array of frames.
                self._frames.append(img)
            else:
                break
        print "Reading complete."
        self._frames = numpy.array(self._frames)