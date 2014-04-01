import logging
import numpy as np

from scipy.signal import convolve2d
from datetime import datetime

class LaplacianPyramid(object):
    """Represents the difference of gaussian pyramid for an image frame.
    
    Attributes:
       frame: An image frame.
       levels: The number of levels you'd like the pyramid to have.
    """

    def __init__(self, frame, levels):
        self._pyramid = []

        # Create the kernel outside the loop, so you only do this once.
        kernel = self.generating_kernel(0.4)

        for channel in range(len(frame[0,0])):
            current_pyramid = []
            reduction_pyramid = []
            expansion_pyramid = []
            channel_frame = frame[:,:,channel]

            reduction_pyramid.append(channel_frame)

            # Reduction
            for x in range(levels):
                out = convolve2d(channel_frame, kernel, 'same')
                channel_frame = out[::2,::2]
                reduction_pyramid.append(channel_frame)

            # Expansion
            for level in range(1, len(reduction_pyramid)):
                current_frame = reduction_pyramid[level]
                out = np.zeros((current_frame.shape[0]*2, current_frame.shape[1]*2))
                out[::2,::2] = current_frame
                # *4 because image becomes 4 times weaker with convolution
                expansion_pyramid.append(4*convolve2d(out, kernel, 'same'))

            # Remove last element.
            del reduction_pyramid[-1]

            # Subtract the pyramids.
            if (len(reduction_pyramid) != len(expansion_pyramid)):
                logging.critical("Pyramid size does not match.")
            else:
                for level in range(len(reduction_pyramid)):
                    reduction = reduction_pyramid[level]
                    expansion = expansion_pyramid[level]
                    laplacian = reduction - expansion[0:reduction.shape[0], 
                                                      0:reduction.shape[1]]
                    current_pyramid.append(laplacian)

            # Append Laplacian Pyramid for the current channel.

            self._pyramid.append(current_pyramid)

    def generating_kernel(self, a):
        '''Returns a 5x5 generating kernel based on parameter a.
        '''
        w_1d = np.array([0.25 - a/2.0, 0.25, a, 0.25, 0.25 - a/2.0])
        return np.outer(w_1d, w_1d)

    @property
    def pyramid(self):
        """Return the Laplacian Pyramid.
        """
        return self._pyramid