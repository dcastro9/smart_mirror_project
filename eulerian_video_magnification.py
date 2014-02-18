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

    def __init__(self, frames, levels=3, step=3, alpha=40):
        """Initializes the video magnification process by obtaining the frames.
        """
        # Split into frames
        self._frames = frames
        self._pyramids = []
        self._levels = levels
        self._alpha = alpha
        # Obtain the Laplacian Pyramid on each frame.

        pyramid_red = []
        pyramid_blue = []
        pyramid_green = []

        for val in range(len(frames)):
            img = frames[val]
            img = img[::step,::step]
            lp = LaplacianPyramid(img, levels)
            pyramid_red.append(lp.pyramid[0])
            pyramid_green.append(lp.pyramid[1])
            pyramid_blue.append(lp.pyramid[2])

        self._pyramids.append(pyramid_red)
        self._pyramids.append(pyramid_blue)
        self._pyramids.append(pyramid_green)
        

    def process(self):
        evm_array = np.zeros(len(self._frames))
        # Index into the frames
        for channel in self._pyramids:
            for level in range(len(channel[0])):
                cur_values = []
                for pyramid in channel:
                    width = len(pyramid[level])
                    height = len(pyramid[level][0])
                    cur_values.append(pyramid[level][width/2,height/2])
                evm_array += \
                    self.__butter_bandpass_filter(cur_values, 0.83, 1, 30)
        # Average the butterworth filter.
        evm_array /= (len(self._pyramids)*self._levels)
        for val in range(len(evm_array)):
            self._frames[val][:,:,2] += evm_array[val]*self._alpha

        return self._frames
        

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
