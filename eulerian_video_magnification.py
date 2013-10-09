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
        self._frames = numpy.array(self._frames)

    def __reduce(_frames):
        '''Reduces each frame of the video to half its size.

        Do I need to create a new numpy array for each reduce or would I overwrite the current
        frames array? I'm not sure if we'd need access to non-reduced ones.

        Also, this is basically just from the HW5 assignment from summer. It contains a
        generating_kernel method, which was defined above it (I'll put it below this function
        for reference). Do we need this/what does it do?
        '''
        for frame in self._frames:
            out = None
            k = generating_kernel(0.4)
            out = scipy.signal.convolve2d(frame,k,'same')
            newFrame = out[::2,::2] #can we just overwrite frame?

    def __generating_kernel(a):
        '''Returns a 5x5 generating kernel with parameter a.

        From HW5 Barcelona.
        '''
        w_1d = numpy.array([0.25 - a/2.0, 0.25, a, 0.25, 0.25 - a/2.0])
        return numpy.outer(w_1d, w_1d)