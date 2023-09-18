"""
Realizar la multiplicación de dos números enteros sin usar la operación producto.
"""

def multiplicar(num1, num2):
    i = 0
    suma = 0
    while i < num2:
        suma = suma + num1
        i = i + 1

    return suma

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))

resultado = multiplicar(num1, num2)

print(f'{num1} x {num2} = {resultado}')