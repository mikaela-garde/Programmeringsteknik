import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

#Första kruvan
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
x = np.sin(theta)
y = np.cos(theta)

ax.plot(x, y, z)

#Andra kruvan
z = np.linspace(-2, 2, 100)
x = -np.sin(theta)
y = -np.cos(theta)

ax.plot(x, y, z)

ax.set_zlim(-1, 1)

plt.show()