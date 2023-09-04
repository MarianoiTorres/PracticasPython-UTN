# Ingresar 3 edades e indicar cuantas son menores de edad 

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