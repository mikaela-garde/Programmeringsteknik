import numpy as np
import matplotlib.pyplot as plt

def q(t, a, b):
    return (np.e**(-t))*(a*np.cos(t) + b*np.sin(t)) + np.cos(t) + np.sin(t)

def f(t):
    return np.cos(t)+2*np.sin(t)

values = np.arange(-4, 5, 1)
t = np.arange(0, 20.1, 0.1)

for a in values:
    for b in values:
        plt.plot(t, q(t, a, b))

plt.plot(t, f(t))
plt.axis([0, 20, -5, 5])
plt.show()

#Den beter sig inte riktigt som den funktionen, den är lite förskjuten och har större amplitud