import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

#UPPGIFT A
a = np.array([[4, -1, -9, -4, -6],
              [1, 1, -1, 4, -5],
              [0, -3, 4, 7, 0],
              [3, -5, -5, -3, 7],
              [9, -1, 4, -8, -9]])
b = np.array([-59, -21, 20, 16, -11])
x = np.linalg.solve(a, b)
print(x)

#UPPGIFT B
x = np.array([1325.9, 1167.3, 1069.1, 992.5, 821.2, 676.3, 548, 515.4,
              476.3, 342, 25.5, 31.3, 150.4, 226, 395.5, 454, 255.1])
y = np.array([28820, 25460, 21810, 20640, 18000, 16300, 14160, 13620,
              13080, 10360, 1360, 1620, 5390, 7680, 12210, 13600, 8430])

A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

plt.plot(x, y, 'o', label='Original data', markersize=10)
plt.plot(x, m*x + c, 'r', label='Fitted line')
plt.legend()
plt.show()

def P(x):
    return m*x+c

def yen_to_sek(x):
    return x*8.5430/100

print("Kostnaden Sendai-Tokyo: " + str(int(P(325.4))) + " JPY.")
print("Kostnaden Stockholm-Göteborg: " + str(int(yen_to_sek(P(455)))) + " Kr.")

#UPPGIFT C

# INGRIDIENSER

ingrediens = np.array(["Carrot", "Potato", "Onion", "Wheat_flour", "Yeast_dry", "Soy_beans", "Hazelnuts", "Apple",
                      "Cabbage", "Tomato", "Broccoli", "Avocado", "Brown_Sugar", "Bananas", "Spinach", "Olive_oil",
                      "Mushrooms", "Milk", "Cheddar", "Eggs", "Pork_Shoulder", "Ground_Beef", "Salmon_fillet",
                      "Chicken_meat", "Chicken_liver"])

# NÄRINGSINNEHÅLL/PRODUKT

A_ub = np.array([[930, 9600, 240, 0.835, 0.066, 0.058, 0.983, 0, 5.9, 0, 0.0132],
                [2000, 17000, 90, 0.0006, 0.08, 0.03, 1.05, 0, 19.7, 0, 0.0019],
                [1100, 9340, 100, 0, 0.046, 0.027, 0.116, 0, 7.4, 0, 0],
                [13700, 72500, 1870, 0, 0.447, 0.215, 6.365, 0, 0, 0, 0],
                [40440, 41220, 7610, 0, 10.99, 4.0, 40.3, 0, 0.3, 0, 0],
                [36490, 30160, 19940, 0.001, 0.874, 0.87, 1.623, 0, 6.0, 0, 0.047],
                [14950, 16700, 60750, 0.001, 0.643, 0.113, 1.8, 0, 6.3, 0, 0.014],
                [260, 13810, 170, 0.003, 0.017, 0.026, 0.091, 0, 4.6, 0, 0.002],
                [1280, 5800, 100, 0, 0.061, 0.040, 0.234, 0, 36.6, 0, 0.076],
                [900, 3900, 200, 0.042, 0.037, 0, 0.594, 0, 14.0, 0, 0.008],
                [2820, 6640, 370, 0.031, 0.071, 0.117, 0.639, 0, 89.2, 0, 0.101],
                [2000, 8530, 14660, 0.007, 0.067, 0.13, 1.738, 0, 10.0, 0, 0.021],
                [0, 97330, 0, 0, 0.008, 0.007, 0.082, 0, 0, 0, 0],
                [1090, 22840, 330, 0, 0.031, 0.073, 0.665, 0, 8.7, 0, 0],
                [2900, 3600, 400, 0.469, 0.078, 0.189, 0.724, 0, 28.0, 0, 0.483],
                [0, 0, 100000, 0, 0, 0, 0, 0, 0, 0, 0.06],
                [3090, 3260, 340, 0, 0.081, 0.402, 3.607, 0.00004, 2.1, 0.002, 0],
                [3220, 5260, 3250, 0.046, 0.044, 0.183, 0, 0.0005, 0, 0.080, 0],
                [24900, 1300, 33100, 0.602, 0.03, 0.320, 0.05, 0.0016, 0, 0.180, 0.003],
                [12600, 1120, 10600, 0.149, 0.066, 0.5, 0.064, 0.001, 0, 0.001, 0.03],
                [19900, 0, 8670, 0.009, 0.79, 0.280, 6.68, 0.007, 0, 0.006, 0],
                [19190, 0, 12440, 0.012, 0.23, 0.2, 4.16, 0.002, 0, 0, 0],
                [20000, 0, 16000, 0.026, 0.120, 0.11, 7.3, 0.004, 0, 0.01, 0],
                [21500, 0, 6900, 0.024, 0.190, 0.15, 12.0, 0.0003, 0, 0.002, 0],
                [19400, 700, 3800, 9.5, 0.48, 2.4, 12.0, 0.032, 33.8, 0.0004, 0]]).transpose()

# TOTALA NÄRINGSMÄNGDEN MAN BEHÖVER

b_ub = np.array([60000, 275000, 70000, 0.7, 1.1, 1.2, 15, 0.002, 75, 0.01, 0.065])

# PRISER

c = np.array([1.95, 0.49, 0.99, 1.20, 31.96, 6.50, 6.95, 0.95,
              0.49, 2.99, 2.69, 5.99, 1.09, 1.99, 2.99, 12.90,
              6.90, 0.99, 17.90, 2.99, 6.99, 7.99, 19.90, 8.99,
              7.99])
# ENERGIINNEHÅLL

A_eq = np.asmatrix(np.array([173, 322, 166, 1418, 1361, 1866, 2629, 219, 103, 74, 141, 670, 1576, 371, 97, 3699,
                 93, 252, 1682, 647, 647, 787, 964, 621, 482]))

# ENERGIBEHOV
B_eq = 8710

# LÖSNING
res = linprog(c, -A_ub, -b_ub, A_eq, B_eq, options={"disp": True, "tol": 1e-10})
print("Kostnaden av menyn:" + str(res.fun) + "SEK\n")
print("Optimala ingridienslistan: ")
for i in range(len(ingrediens)):
    if res.x[i] != 0:
        print(ingrediens[i] + ": " + str(res.x[i]*100) + "g")


#VEGAN
A_ub_veg = np.delete(A_ub, np.s_[17:24], 1)
vegan_supplements = np.array([[0], [0], [0], [0], [0], [0], [0], [2], [0], [10], [0]])
A_ub_veg = np.append(A_ub_veg, vegan_supplements, 1)

c_veg = np.delete(c, np.s_[17:24], 0)
c_veg = np.append(c_veg, np.array([1000]), 0)

A_eq_veg = np.delete(A_eq, np.s_[17:24], 1)
A_eq_veg = np.append(A_eq_veg, np.array([[0]]), 1)

veg_ingrediens = np.array(["Carrot", "Potato", "Onion", "Wheat_flour", "Yeast_dry", "Soy_beans", "Hazelnuts", "Apple",
                      "Cabbage", "Tomato", "Broccoli", "Avocado", "Brown_Sugar", "Bananas", "Spinach", "Olive_oil",
                      "Mushrooms", "Vegan_supplement"])

#VEGLÖSNING
res_veg = linprog(c_veg, -A_ub_veg, -b_ub, A_eq_veg, B_eq, options={"disp": True, "tol": 1e-10})
print("Veganskt:")
print("Kostnaden av menyn:" + str(res_veg.fun) + "SEK\n")
print("Optimala ingridienslistan: ")
for i in range(len(veg_ingrediens)):
    if res_veg.x[i] != 0:
        print(veg_ingrediens[i] + ": " + str(res_veg.x[i]*100) + "g")
