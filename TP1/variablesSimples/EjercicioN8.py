"""
Mara y Juan son hermanos y recibirán un regalo dependiendo de sus notas en la escuela.
Sus padres les dijeron: “Si tienen una nota inferior a 6 no hay regalo. Si sacan una nota 
entre 6 y 7 reciben una comida en un bar a elegir. Entre 7 y 9, una ropa a elección.
Para una nota 10, reciben ambos regalos. ¿Qué regalo obtuvo cada uno?
"""

Mara = int(input('Cual es la nota de Mara?: '))
Juan = int(input('Cual es la nota de Juan?: '))


if Mara < 6: 
    print('Mara no recibe ningun regalo')
else:
    if Mara >= 6 and Mara <=7:
        print('Mara recibe una comida en un bar')
    elif Mara > 7 and Mara <= 9:
        print('Mara recibe una ropa a eleccion')
    else:
        print('Mara recibe una comida en un bar y una ropa a eleccion')

if Juan < 6: 
    print('Juan no recibe ningun regalo')
else:
    if Juan >= 6 and Juan <=7:
        print('Juan recibe una comida en un bar')
    elif Juan > 7 and Juan <= 9:
        print('Juan recibe una ropa a eleccion')
    else:
        print('Juan recibe una comida en un bar y una ropa a eleccion')