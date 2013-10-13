
class LaplacianPyramid(object):
    """Represents the difference of gaussian pyramid for an image frame.
    
    Attributes:
       frame: The location of the video you wish to process.
       levels: The number of levels you'd like the pyramid to have.
    """

    def __init__(self, frame, levels):
        self._pyramid = []
        self._pyramid.append(frame)

        # Create the kernel outside the loop, so you only do this once.
        kernel = __generating_kernel(0.4)

        # The idea here is to do the reduction and expansion automatically
        # so we have a pyramid already generated, right now I'm just doing the
        # reduction, but we can add the expansion right after in the loop.
        for x in range(levels):
            out = scipy.signal.convolve2d(frame, kernel, 'same')
            frame = out[::2,::2]
            self._pyramid.append(frame)
    
    def __generating_kernel(a):
        '''Returns a 5x5 generating kernel based on parameter a.
        '''
        w_1d = numpy.array([0.25 - a/2.0, 0.25, a, 0.25, 0.25 - a/2.0])
        return numpy.outer(w_1d, w_1d)
