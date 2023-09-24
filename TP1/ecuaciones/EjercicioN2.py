# Encontrar dos números cuya suma sea 45 y cuya resta sea 21.

'''
x + y = 45
x - y = 21

x = 45 - y

(45 - y) - y = 21
45 - 2y = 21
45 = 21 + 2y
45 - 21 = 2y
24/2 = y
'''
num1 = (45 - 21) // 2
num2 = 45 - num1

print(f'La suma de {num1} y {num2} es igual a 45 y su diferencia es 21')

