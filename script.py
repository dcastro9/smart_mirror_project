import scipy

from eulerian_video_magnification import EulerianVideoMagnification
from laplacian_pyramid import LaplacianPyramid

evm = EulerianVideoMagnification("sample.mp4")
print "Done processing video."
laplacian = LaplacianPyramid(evm._frames[0], 5)
for level in range(len(laplacian._pyramid)):
    scipy.misc.imsave('out' + str(level) + '.jpg', laplacian._pyramid[level])