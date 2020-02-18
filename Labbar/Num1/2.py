import numpy as np
import math

vektor_a = np.arange(1,6, 1)
vektor_b = np.arange(0, 2*math.pi, 0.1)
matris_c = np.array([[1, 2], [3, 4], [5, 6]])
vektor_d = np.array(vektor_a.tolist() + [6, 7])
matris_e = np.array([vektor_a.tolist(), (vektor_a*-1).tolist()])
vektor_f = np.sin(vektor_b)

#UPPGIFT 2
def function_a(x):
    return x*x


def function_b1(x):
    return x*x


def function_b2(x):
    return(x@x)


def function_c1(x):
    return x*x


def function_c2(x):
    return x@x

print(function_c1(matris_c))