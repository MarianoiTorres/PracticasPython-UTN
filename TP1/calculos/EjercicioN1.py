# sume dos vectores generados al azar

import numpy as np

array1 = np.random.randint(0, 100, size=5)
array2 = np.random.randint(0, 100, size=5)

i = 0
total = 0
while i < len(array1):
    total = total + array1[i]
    total = total + array2[i]
    i = i + 1
    
print(array1)
print(array2)
print(total)