"""
Alberto y su padre se llevan 25 años de edad. 
Calcular la edad de Alberto sabiendo que dentro 
de 15 años la edad de su padre será el doble que la suya.
"""

for edad_alberto in range(9, 101):

    edad_padre = edad_alberto + 25

    if edad_padre + 15 == 2 * (edad_alberto + 15):
        break

print("La edad actual de Alberto es:", edad_alberto)
print("La edad actual del padre es:", edad_padre)