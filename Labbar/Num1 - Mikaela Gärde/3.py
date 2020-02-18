import numpy as np
import matplotlib.pyplot as plt

#UPPGIFT 3
def uppg3(x):
    return 1+x+4/(x-2)**2

def uppg3_a1(x):
    return x+1

x = np.arange(-10, 10.1, 0.1)
plt.plot(x, uppg3(x))
plt.plot(x, uppg3_a1(x))
plt.plot([2, 2], [-10, 10])

plt.axis([-10, 10, -10, 10])
plt.show()
