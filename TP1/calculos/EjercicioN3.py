'''
a partir de una lista de 12 números generar una matriz de 3 filas por cuatro columnas (3x4),
elevar al cuadrado cada elemento de dicha matriz. Mostrar ambas matrices.
'''

import numpy as np

lista = np.random.randint(0, 12, size=12)

listaElevada = lista ** 2

matriz = np.reshape(lista, (3, 4))
matrizElevada = np.reshape(listaElevada, (3, 4))

print(matriz)
print('\n')
print(matrizElevada)