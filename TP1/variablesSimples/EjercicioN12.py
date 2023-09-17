"""
Dado el número del mes, indicar su nombre respectivo en caso de ser posible.
"""

mes = int(input('Ingrese el numero del mes que desea saber el nombre: '))

if mes > 0 and mes <= 12:
    if mes == 1: nombre = 'Enero'
    if mes == 2: nombre = 'Febrero'
    if mes == 3: nombre = 'Marzo'
    if mes == 4: nombre = 'Abril'
    if mes == 5: nombre = 'Mayo'
    if mes == 6: nombre = 'Junio'
    if mes == 7: nombre = 'Julio'
    if mes == 8: nombre = 'Agosto'
    if mes == 9: nombre = 'Septiembre'
    if mes == 10: nombre = 'Octubre'
    if mes == 11: nombre = 'Noviembre'
    if mes == 12: nombre = 'Deciembre'

    print(f"El numero {mes} es equivalente al mes {nombre}")
else:
    print('Debe ingresar un numero de mes valido')