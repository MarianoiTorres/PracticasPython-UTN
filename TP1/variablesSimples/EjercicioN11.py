"""
En un salón de clases de 50 niños y niñas, a 10 les gusta solo el helado de fresa 
y a 5 solo el helado de chocolate.  Si a 20 niños no les gusta el helado ni de 
fresa ni de chocolate: ¿a cuántos niños les gustan los dos helados?, ¿a cuántos 
niños les gusta en total el helado de fresa?, ¿a cuántos el de chocolate?
"""

ambos_helados = 50 - 10 - 5 - 20

fresa = ambos_helados + 10

chocolate = ambos_helados + 5

print(f'A {ambos_helados} niños les gusta ambos helados')
print(f'A {fresa} niños les gusta solo el helado de fresa')
print(f'A {chocolate} niños les gusta solo el helado de chocolate')

