from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import pylab

from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# punkter som utgör pyramiden
v = np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1],  [-1, 1, -1], [0, 0, 1]])
ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

# generera sidorna
verts = [ [v[0], v[1], v[4]], [v[0], v[3], v[4]],
 [v[2], v[1], v[4]], [v[2], v[3], v[4]], [v[0], v[1], v[2], v[3]]]

# plotta sidorna
ax.add_collection3d(Poly3DCollection(verts))

plt.show()