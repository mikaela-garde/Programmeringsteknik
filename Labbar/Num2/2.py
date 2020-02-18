import math
from scipy import ndimage as ndi
import matplotlib.pyplot as plt
import numpy as np

bild = plt.imread("blomma.png")
bild_svartvit = np.zeros((bild.shape[0], bild.shape[1]))

for i in range(bild.shape[0]):
    for j in range(bild.shape[1]):
        medel = (bild[i,j][0]+bild[i,j][1]+bild[i,j][2])/3
        bild_svartvit[i, j] = medel

plt.imshow(bild_svartvit, cmap="gray")
plt.show()

gx = np.array([[-1, 0, 1],
      [-2, 0, 2],
      [-1, 0, 1]])
gy = np.array([[-1, -2, -1],
      [0, 0, 0],
      [1, 2, 1]])

xd = ndi.convolve(bild_svartvit, gx, mode='constant')
yd = ndi.convolve(bild_svartvit, gy, mode='constant')

for i in range(bild_svartvit.shape[0]):
    for j in range(bild_svartvit.shape[1]):
        bild_svartvit[i, j] = np.sqrt((xd[i, j]**2)+(yd[i, j]**2))

bild_svartvit[bild_svartvit*255 > 100] = 0
bild_svartvit[bild_svartvit*255 < 60] = 1

plt.imshow(bild_svartvit, cmap="gray")
plt.show()

m = np.ones(shape=(5, 5))

f = ndi.convolve(bild_svartvit, m, mode='constant')

f[5**2] = 1
f[f != 5**2] = 0

for i in range(bild_svartvit.shape[0]):
    for j in range(bild_svartvit.shape[1]):
       bild_svartvit[i, j] = f[i, j]

plt.imshow(bild_svartvit, cmap="gray")
plt.show()

