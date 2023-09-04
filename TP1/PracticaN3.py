# Simular la potenciacion con numeros enteros

def potencia (num, exp):
    i = 1
    resultado = num
    while i < exp:
        mult =  resultado * num
        resultado = mult
        print(resultado)
        i = i + 1
    
    return resultado

num = int(input('Ingrese un numero: '))
exp = int(input('Ingrese el exponente de ese numero: '))

resultado = potencia(num, exp)

print(f"La potencia de {num} elevado a {exp} es de : {resultado}")
