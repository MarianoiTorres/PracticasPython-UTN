"""
A partir de un sueldo básico, un empleado recibe $40.000 por asistencia perfecta,
$5.000 por cada hora extra, descuentos de jubilación 11%, 2% por obra social 
y por cada año de antigüedad $8.000. ¿Cuánto ganará finalmente? Dibuje en modo
consola algo similar a una boleta de liquidación de haberes.
"""

basico = int(input('Ingrese su sueldo basico: '))
asistencia = int(input('Usted tuvo una asistencia del 100%? (1 = si / 2 = no):'))
horas = int(input('Cuantas horas extras realizo?: '))
años = int(input('Cuantos años de antiguedad tiene?: '))

descuentoJubilacion = basico * 0.11
descuentoObra = basico * 0.02
bonoHoras = 5000 * horas
bonoAntiguedad = 8000 * años
bonoAsistencia = 0
if asistencia == 1:
    bonoAsistencia = 40000

total = basico + bonoAsistencia + bonoAntiguedad + bonoHoras - descuentoJubilacion - descuentoObra

print('====== Boleta de liquidacion de haberes ======\n')
print(f"Sueldo basico: {basico} \n" )
print("===== Beneficios ===== \n")
print(f"Bono por Asistencia Perfecta: {bonoAsistencia} \n" )
print(f"Bono por Horas Extras: {bonoHoras} \n" )
print(f"Bono por Años de Antiguedad: {bonoAntiguedad} \n" )
print('===== Descuentos ======')
print(f"Descuento por Jubilacion: {descuentoJubilacion} \n" )
print(f"Descuento por Obra social: {descuentoObra} \n" )
print('===== TOTAL ===== \n')
print(f'Total: {total}')






