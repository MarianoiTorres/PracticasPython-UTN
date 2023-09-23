'''
Un pendrive tiene un precio de $50. Como promoción si se compran más de 12 unidades
ya el precio tiene un descuento del 10%. Simular un par de ventas y representar 
gráficamente las ecuaciones correspondientes
'''

import matplotlib.pyplot as plt
import numpy as np

ventas = np.random.randint(1, 15, size=2)
precios_totales = []

for venta in ventas:
    if venta >= 12:
        total = venta * 50
        total = total - (total * 10) / 100
        precios_totales.append(total)
    else:
        total = venta * 50
        precios_totales.append(total)


plt.figure(figsize=(8, 6))
plt.plot(ventas, precios_totales, color='blue', marker='o')
plt.grid(True)
plt.show()

