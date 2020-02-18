import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

a = np.array([ [0,0,0], [1, 1, 1], [0, 1, 1] ])
vertices = [ a[0], a[1], a[2] ]

ax.add_collection3d(Poly3DCollection(vertices, facecolors='green', edgecolors='blue'))

plt.show()

#Komplexa tal
print(1j * 1j)
c = complex(1, 2)
print(type(c))
c.conjugate()
abs(c)
print(c.imag)
print(c.real)
