"""
Dada la cantidad de días de un mes indicar que mes podría ser (en caso de ser posible).
"""

dias = int(input('Ingrese la cantidad de dias del mes: '))

if dias >= 28 and dias <= 31:
    if dias == 30: meses = 'Abril, Junio, Septiembre y Noviembre'
    if dias == 31: meses = 'Enero, Marzo, Mayo, Julio, Agosto, Octubre y Diciembre'
    if dias == 28 or dias == 29: meses = 'Febrero'

    print(f'Los meses con la cantidad de {dias} dias son: {meses}')
else:
    print(f'No existe ningun mes con {dias} dias')