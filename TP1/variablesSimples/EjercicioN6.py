"""Calcular el volumen de una esfera de diámetro conocido."""

diametro = int(input('Ingrese el diametro de la esfera: '))

radio = diametro / 2

volumen = (4/3) * 3.1416 * radio ** 3

print(f'El volumen de una esfera con un diametro de {diametro} es {volumen}')