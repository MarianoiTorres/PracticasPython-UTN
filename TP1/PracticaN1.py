# Ingresar 3 edades e indicar cuantas son menores de edad 

"""
edad1 = int(input("Ingrese la edad de la primera persona: "))
edad2 = int(input("Ingrese la edad de la segundo persona: "))
edad3 = int(input("Ingrese la edad de la tercera persona: "))

def menoresDeEdad (edad):

    resultado = ''

    if edad < 18:
        resultado = 'Es menor de edad'
    else: 
        resultado = 'Es mayor de edad'

    return resultado

print(menoresDeEdad(edad1))
print(menoresDeEdad(edad2))
print(menoresDeEdad(edad3))

"""

edades = []

def menoresDeEdad():
    while True:
        edades_str = input("Ingrese una edad o presiones 'x' para terminar: ")
        if edades_str.lower() == 'x':
            break
        else: 
            edad = int(edades_str)  # convierte a entero el string
            edades.append(edad)  #es como el push 
            

menoresDeEdad()

def cantidad():
    i = 0
    contador = 0
    while i < len(edades):  # len = length
        if edades[i] < 18: 
            contador = contador + 1
        i = i + 1

    return contador       

menores = str(cantidad())  # convierte entero en string
print(f"La cantidad de personas menores de edad es de {menores}")