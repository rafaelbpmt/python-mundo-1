import math

numero = int(input('digite um numero: '))
raiz = math.sqrt(numero)
print(f'a raiz de {numero} é igual a {math.ceil(raiz)}') # math.ceil arredonda a raiz pra cima 

import random
# numeroAleatorio = random.random() - gera numero aletório entre 0 e 1
numeroAleatorio = random.randint(1, 10) # gera numero aleatório entre os números selecionados, no caso, entre 1 e 10
print(numeroAleatorio)

# ceil
# floor
# trunc
# pow
# sqrt
# factorial