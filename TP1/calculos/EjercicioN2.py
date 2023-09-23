# generar el azar un vector, luego multiplique por -2  a cada elemento del vector

import numpy as np

array = np.random.randint(0, 1000, size=5)

i = 0
while i < len(array):
    array[i] = array[i] * -2
    i = i + 1

print(array)