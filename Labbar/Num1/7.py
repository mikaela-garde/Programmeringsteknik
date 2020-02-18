import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import math

x = np.arange(-10, 10.1, 0.1)
plt.plot(x, np.sin(x))

def taylor(x):
    value = 0
    j = 1
    for i in range(1,14, 2):
        value += ((-1)**(j+1))*(x**i)/sp.factorial(i)
        j+=1
    return value

plt.plot(x, taylor(x))
plt.axis([-10, 10 , -10, 10])
plt.show()

#approximationen är bra för alla x mellan ca -4.5 och 4.5
