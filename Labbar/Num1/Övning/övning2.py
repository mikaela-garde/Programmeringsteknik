import numpy as np
import matplotlib.pyplot as plt

my_big_array = np.zeros((100, 100, 3))
my_big_array[80,20] = [100, 0, 0]
my_big_array[90,20] = [0, 100, 0]
my_big_array[70,20] = [0, 0, 100]
plt.imshow(my_big_array)
plt.show()