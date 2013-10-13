
class LaplacianPyramid(object):
    """Represents the difference of gaussian pyramid for an image frame.
    
    Attributes:
       frame: The location of the video you wish to process.
       levels: The number of levels you'd like the pyramid to have.
    """

    def __init__(self, frame, levels):
        self._pyramid = []
        self._pyramid.append(frame)

        for x in range(levels):
            frame = frame[::2,::2,:]
            self._pyramid.append(frame)
