"""
Dadas las longitudes de tres segmentos (a,b,c),
determinar qué triángulo forman, en caso de ser posible.
"""

print('Ingrese la longitud de cada segmento: ')

a = int(input('Segmento A: '))
b = int(input('Segmento B: '))
c = int(input('Segmento C: '))

if a + b >= c and a + c >= b and b + c >= a:
    if a == b == c:
        print('Es un triangulo equilatero')
    elif a != b and a != c and b != c:
        print('Es un triangulo escaleno')
    else:
        print("Es un triangulo isosceles")
else:
    print('Las longitudes de cada segmenteo que ingreso no pueden formar un triangulo')