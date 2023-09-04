#Ingresar el lado de un rectangulo y calcular su perimetro y area

def calcular (base, altura):
    return (base * altura, 2 * (base + altura))

base = int(input('Ingrese la base del rectangulo: '))
altura = int(input('Ingrese la altura del rectangulo: '))

resultado = calcular(base, altura)

print("El perimetro del rectangulo es de: {}".format(resultado[0]), "Y el area es de: {}".format((resultado[1])))