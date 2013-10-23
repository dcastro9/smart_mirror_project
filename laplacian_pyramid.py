import logging
import numpy as np

from scipy.signal import convolve2d

class LaplacianPyramid(object):
    """Represents the difference of gaussian pyramid for an image frame.
    
    Attributes:
       frame: The location of the video you wish to process.
       levels: The number of levels you'd like the pyramid to have.
    """

    def __init__(self, frame, levels):
        self._pyramid = []
        reduction_pyramid = []
        expansion_pyramid = []
        frame = frame[:,:,0]

        reduction_pyramid.append(frame)

        # Create the kernel outside the loop, so you only do this once.
        kernel = self.generating_kernel(0.4)

        # Reduction
        for x in range(levels):
            out = convolve2d(frame, kernel, 'same')
            frame = out[::2,::2]
            reduction_pyramid.append(frame)

        # Expansion
        for level in range(1, len(reduction_pyramid)):
            current_frame = reduction_pyramid[level]
            out = np.zeros((current_frame.shape[0]*2, current_frame.shape[1]*2))
            out[::2,::2] = current_frame
            # 4 times because image would be 4 times weaker otherwise w/ conv.
            expansion_pyramid.append(4*convolve2d(out, kernel, 'same'))

        # Oh Python.
        del reduction_pyramid[-1]

        # Subtract the pyramids.
        if (len(reduction_pyramid) != len(expansion_pyramid)):
            logging.critical("Pyramid size does not match - cannot continue.")
        else:
            for level in range(len(reduction_pyramid)):
                reduction = reduction_pyramid[level]
                expansion = expansion_pyramid[level]
                laplacian = reduction - expansion[0:reduction.shape[0], 
                                                  0:reduction.shape[1]]
                self._pyramid.append(laplacian)


    def generating_kernel(self, a):
        '''Returns a 5x5 generating kernel based on parameter a.
        '''
        w_1d = np.array([0.25 - a/2.0, 0.25, a, 0.25, 0.25 - a/2.0])
        return np.outer(w_1d, w_1d)
