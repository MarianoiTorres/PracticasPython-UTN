"""Dado la base y la altura de un triángulo, calcular su área."""

base = int(input('Ingrese la base del triangulo: '))
altura1 = int(input('Ingrese la altura 1 del triangulo: '))
altura2 = int(input('Ingrese la altura 2 del triangulo: '))

if altura1 == altura2:
    area = base * altura1 / 2
    print(f'El area del triangulo es {area}')
else:
    print('Las dos alturas tienen que ser iguales')