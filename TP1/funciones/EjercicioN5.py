"""
Ingresar base y exponente enteros positivos. Calcular la potencia. (función)
"""

def potencia(base, exponente):
    if base < 0 and exponente < 0:
        return 'Solo se permiten valores positios'
    
    if exponente == 0:
        return 1
    else: 
        return base ** exponente
    
base = int(input('Ingrese la base: '))
exponente = int(input('Ingrese el exponente: '))

resultado = potencia(base, exponente)

print(f"{base}^{exponente} = {resultado}")