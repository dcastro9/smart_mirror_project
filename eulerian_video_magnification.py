import numpy as np

from cv2 import VideoCapture
from laplacian_pyramid import LaplacianPyramid
from scipy.signal import butter
from scipy.signal import lfilter

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
        
        # Obtain the Laplacian Pyramid
        while True:
            success, img = video.read()
            if success:
                img = img[::3,::3]
                self._frames.append(LaplacianPyramid(img, levels)._pyramid)
            else:
                break
        self._frames = np.array(self._frames)



    """The below helper functions implement a butterworth filter.

    This code was taken directly from http://bit.ly/1d8nYPC
    """
    def __butter_bandpass(self, lowcut, highcut, fs, order=2):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a


    def butter_bandpass_filter(self, data, lowcut, highcut, fs, order=2):
        b, a = self.__butter_bandpass(lowcut, highcut, fs, order=order)
        y = lfilter(b, a, data)
        return y