"""
indicar si un número es primo. En caso de no serlo indicar en qué valores es divisible
"""

def esPrimo(numero):
    i = 2
    nose = []
    while i < numero:
        if numero % i == 0:
            nose.append(i)
        i = i + 1

    if len(nose) == 0:
        return 'es un numero primo'
    else:
        return nose
    
numero = int(input('Ingrese un numero para saber si es primo: '))

resultado = esPrimo(numero)

if type(resultado) == str:
    print(f'El numero {numero} {resultado}')
else:
    print(f'El numero ingresado no es un numero primo')
    print(f'porque es disivible por los siguientes numeros: {resultado}')
    