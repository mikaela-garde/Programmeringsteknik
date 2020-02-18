import numpy as np
import math
import matplotlib.pyplot as plt
from itertools import combinations

# UPPGIFT A
def mandelbrot(c):
    z = 0
    for i in range(1, 101): # körs 100 gånger
        if abs(z) > 2: # om avståndet mellan komplexa planet & xy-planet är större än 2: break
            return False
        else:
            z = z*z + c # det är någonting här som är fel tror jag!!
    return True

#print(mandelbrot(2j))


# UPPGIFT B
M = np.zeros((401, 401))
a = b = np.arange(-2, 2, 0.01)


def draw(a, b):
    for i in a:
        for j in b:
            if mandelbrot(i + j*1j):
                M[int((i+2)*100), int((j+2)*100)] = 1

#draw(a, b)

# UPPGIFT C
c = d = np.arange(0, 0.4, 0.001)
#draw(c, d)
#plt.imshow(M, cmap='gray')
#plt.show()

e = f = np.arange(-0.001, 0.003, 0.0001)
draw(e, f)
plt.imshow(M, cmap='gray')
plt.show()


