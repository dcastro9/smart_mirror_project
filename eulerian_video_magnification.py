import numpy as np

from cv2 import VideoCapture
from laplacian_pyramid import LaplacianPyramid
from scipy.signal import butter
from scipy.signal import lfilter

class EulerianVideoMagnification(object):
    """Performs Eulerian Video Magnification.

    TODO(dcastro): Modify to return a list of values given a list of
    image frames.

    Example:
        evm = EulerianVideoMagnification("path/to/video/file")
        evm.run()
    
    Attributes:
       frames: The frames of the video.
       levels: The number of levels you want to compute in the pyramid.
       step: The amount you want the original video to be reduced in size prior
             to computation. Set step=1 if you want to use the original size.
    """

    def __init__(self, frames, levels=2, step=3):
        """Initializes the video magnification process by obtaining the frames.
        """
        # Split into frames
        self._frames = frames

        # Obtain the Laplacian Pyramid on each frame.
        for val in range(len(frames)):
            img = frames[val]
            img = img[::step,::step]
            self._frames.append(LaplacianPyramid(img, levels)._pyramid)

        # Convert to a numpy array.
        self._frames = np.array(self._frames)

    def run(self):
        # Index into the frames
        print self._frames
        #return __butter_bandpass_filter(, 0.83, 1.0, 30)
        

    """The below helper functions implement a butterworth filter.

    This code was taken directly from http://bit.ly/1d8nYPC
    """
    def __butter_bandpass(self, lowcut, highcut, fs, order=2):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        b, a = butter(order, [low, high], btype='band')
        return b, a


    def __butter_bandpass_filter(self, data, lowcut, highcut, fs, order=2):
        b, a = self.__butter_bandpass(lowcut, highcut, fs, order=order)
        y = lfilter(b, a, data)
        return y
