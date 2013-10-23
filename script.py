import scipy

from datetime import datetime
from eulerian_video_magnification import EulerianVideoMagnification
from laplacian_pyramid import LaplacianPyramid

print datetime.now()
evm = EulerianVideoMagnification("sample.mp4", 5)
print datetime.now()

for frame in range(len(evm._frames)):
    current_frame = evm._frames[frame]
    scipy.misc.imsave('out' + str(frame) + '.jpg', current_frame._pyramid[0])