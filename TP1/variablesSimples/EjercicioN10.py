"""
Dado tres números determinar cuántos son iguales
"""

print('Ingrese 3 numeros: \n')
num1 = int(input('Primer numero: '))
num2 = int(input('Segundo numero: '))
num3 = int(input('Tercer numero: '))

if num1 == num2 == num3:
    print('Los 3 numeros son iguales')
elif num1 == num2 or num2 == num3 or num1 == num3:
    print('Hay 2 numeros iguales')
else:
    print('No hay ningun numero igual')