nome = input('insira seu nome: ')

print(f'nome em maiusculo: {nome.upper()}')
print(f'nome em minusculo: {nome.lower()}')
print(f'comprimento do nome: {len(nome)}')
print(f'letras do primeiro nome: {(nome.split(' ', 1) [0])}')