"""
Dadas dos fechas indicar cuántos días hay entre ellas.
"""

primerMes = int(input('Ingresa el numero de mes de la primera fecha: '))
primerDia = int(input('Ingresa el dia de la primera fecha: '))

segundoMes = int(input('Ingresa el numero del segundo mes: '))
segundoDia = int(input('Ingresa el dia de la segunda fecha: '))

meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

i = primerMes
dias = 0

while i <= segundoMes:
    dias = dias + meses[i - 1]

    if i == primerMes:
        dias = dias - primerDia

    if i == segundoMes and i != primerMes:
        dias = dias - segundoDia

    i = i + 1
    
print(f'Diferencia de dias: {dias}')
