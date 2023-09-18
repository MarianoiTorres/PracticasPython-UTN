"""
Realizar el cociente de dos números enteros sin usar la operación división.
"""

def cociente(dividendo, divisor):

    cont = 0
    while dividendo > 0:
        dividendo = dividendo - divisor
        cont = cont + 1
    
    return cont

dividendo = int(input('Ingrese el dividendo: '))
divisor = int(input('Ingrese el divisor: '))

resultado = cociente(dividendo, divisor)

print(f'El cociente de la division de {dividendo} y {divisor} es: {resultado}')