#Ingresar un entero de por lo menos 3 digitos y contar los mismos

def suma (num):
    suma = 0
    while num > 1:
        resto = num % 10  # calcula el resto
        num = num // 10   # divide y el resultado es un entero
        suma = suma + resto  # suma los restos

    return suma

numero = int(input("Ingrese un numero de mas de 3 digitos: "))

resultado = suma(numero)
print(f"La suma de los digitos es {resultado}")
