dia = int(input('quantos dias de aluguel? '))
dia = dia * 60
km = float(input('quantos km rodados? '))
km = km * 0.15

resultado = dia + km

print(f'O total a pagar é de R${resultado}')