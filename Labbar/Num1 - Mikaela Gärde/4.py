import numpy as np
import matplotlib.pyplot as plt

#UPPGIFT 4
def uppg4(x):
    return 1+np.sin(x)+0.5*np.cos(4*x)

def uppg4_numerisk_der(x, h):
    return (uppg4(x+h)-uppg4(x))/h

def uppg4_analytisk_der(x):
    return np.cos(x)-2*np.sin(4*x)

x = np.arange(-2,2 , 0.1)
plt.plot(x, uppg4_analytisk_der(x))
plt.plot(x, uppg4_numerisk_der(x, 0.01))
plt.axis([-2, 2, -4, 4])
plt.show()