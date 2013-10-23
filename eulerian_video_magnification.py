import numpy

from cv2 import VideoCapture
from laplacian_pyramid import LaplacianPyramid

class EulerianVideoMagnification(object):
    """Provides a wrapper for Eulerian Video Magnification processing.

    Example:
        evm = EulerianVideoMagnification("path/to/video/file")
        evm.run()
    
    Attributes:
       video_path: The location of the video you wish to process.
    """

    def __init__(self, video_path, levels):
        """Initializes the video magnification process by obtaining the frames.
        """
        self._video_path = video_path
        self._frames = []        # Split into frames
        video = VideoCapture(video_path)
        while True:
            success, img = video.read()
            if success:
                img = img[::3,::3]
                self._frames.append(LaplacianPyramid(img, levels))
            else:
                break