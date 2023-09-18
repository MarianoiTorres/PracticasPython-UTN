"""
Sumar los dígitos de un entero de más de dos dígitos.
"""

def sumarDigitos(numero):
    i = 0
    suma = 0

    while numero > 0:
        suma = suma + (numero % 10)
        numero = numero // 10  
        i = i + 1
    
    return suma

numero = int(input('Ingrese un numero de mas de 2 digitos: '))

resultado = sumarDigitos(numero)

print(f'La suma de los digitos de {numero} es igual a {resultado}')