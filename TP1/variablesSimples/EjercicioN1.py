'''
Maria, Jorge y Ana deciden que para pagar el almuerzo el sábado,
la cuenta será abonada por el que más lejos esté del porcentaje 
de la humedad de ese día. Quién pagará
'''

Humedad = int(input('Ingrese el porcentaje de humedad: '))

Maria = 50 - Humedad
Jorge = 30 - Humedad
Ana = 80 - Humedad

if Maria * Maria > Jorge * Jorge and Maria * Maria > Ana * Ana:
    print('Maria paga la cuenta')
elif Jorge * Jorge > Maria * Maria and Jorge * Jorge > Ana * Ana:
    print('Jorge paga la cuenta')
else:
    print('Ana paga la cuenta')

