"""Ingresar un número e indicar si es par o impar(en caso de ser posible)"""

numero = int(input('Ingrese un numero: '))

if numero % 2 == 0:
    print(f'El numero {numero} es par')
else:
    print(f'El numero {numero} es impar')
