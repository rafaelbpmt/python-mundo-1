import math

oposto = float(input('insira o cateto oposto: '))
adjacente = float(input('insira o cateto adjacente: '))
formula1 = (oposto ** 2) + (adjacente ** 2)

resultado = math.sqrt(formula1)

print(f'o comprimento da hipotenusa é igual a {resultado}')