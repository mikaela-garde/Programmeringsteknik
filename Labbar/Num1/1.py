import numpy as np
import math

#UPPGIFT 1
vektor_a = np.arange(1,6, 1)
vektor_b = np.arange(0, 2*math.pi, 0.1)
matris_c = np.array([[1, 2], [3, 4], [5, 6]])
vektor_d = np.array(vektor_a.tolist() + [6, 7])
matris_e = np.array([vektor_a.tolist(), (vektor_a*-1).tolist()])
vektor_f = np.sin(vektor_b)

print(vektor_a)
print(vektor_b)
print(matris_c)
print(vektor_d)
print(matris_e)
print(vektor_f)