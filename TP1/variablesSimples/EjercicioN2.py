"""El que parte y reparte se queda con la mejor parte"""

nombre1 = input('Ingrese el nombre de la primera persona: ')
nombre2 = input('Ingrese el nombre de la segunda persona: ')

quienParte = input('Quien parte?')

if nombre1 == quienParte:
    print(f"Tiene que repartir {nombre2}")
else:
    print(f"Tiene que repartir {nombre1}")