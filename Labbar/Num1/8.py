import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

x = np.arange(-10, 10, 0.1)

plt.plot(x, x)
plt.plot(x, np.sin(x))
plt.show()

def f(x):
    return x-np.cos(x)

def f_der(x):
    return 1+np.sin(x)

def binary_search(a, b):
    c = 0
    while np.abs(a-b) > 10**(-12):
        c = (a+b)/2
        if f(c) < 0:
            a = c
        elif f(c) > 0:
            b = c
    return "Med intervallhalvering får man lösningen x=" + str(c) + " med felet: " + str((10**-(12))/2)

def newton_raphsons(x):
    felterm = f(x)/f_der(x)
    x = x-felterm
    while np.abs(x-(x-felterm)) > 10**(-12):
        felterm = f(x)/f_der(x)
        x = x-felterm
    return "Med Newton-Raphson får man lösningen x=" + str(x) + " med felet: " + str(felterm)


print(binary_search(-1, 1))

print(newton_raphsons(-1))

#d) Intervallhalvering kräver flest iterationer



