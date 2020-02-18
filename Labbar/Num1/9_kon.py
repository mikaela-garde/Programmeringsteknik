from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')

r = np.linspace(0, 1, 50)
v = np.linspace(0, 2*np.pi, 50)
r, v = np.meshgrid(r, v)
Z = 1-r

X, Y = r*np.cos(v), r*np.sin(v)

#Plotta ytan
ax.plot_surface(X, Y, Z, cmap=plt.cm.YlGnBu_r)

ax.set_zlim(-1, 1)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
#fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

