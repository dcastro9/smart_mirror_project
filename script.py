import numpy as np
import matplotlib.pyplot as plt
import scipy

from datetime import datetime
from eulerian_video_magnification import EulerianVideoMagnification
from laplacian_pyramid import LaplacianPyramid

evm = EulerianVideoMagnification("sample.mp4", 5)

d1 = []
d2 = []
d3 = []

for frame in evm._frames:
    top_level = frame[0] # Top level of the pyramid.
    d1.append(top_level[88,10]) # Pixel location near forehead.
    d2.append(top_level[88,30]) # Pixel location near nose.
    d3.append(top_level[0,100]) # Pixel not in face.

d1_out = evm.butter_bandpass_filter(d1, 0.83, 1, 30, order=2)
d2_out = evm.butter_bandpass_filter(d2, 0.83, 1, 30, order=2)
d3_out = evm.butter_bandpass_filter(d3, 0.83, 1, 30, order=2)

# Pixel in face 1.
plt.plot(d1)
plt.plot(d1_out)
plt.show()

# Pixel in face 2.
plt.plot(d2)
plt.plot(d2_out)
plt.show()

# Pixel not in face.
plt.plot(d3)
plt.plot(d3_out)
plt.show()