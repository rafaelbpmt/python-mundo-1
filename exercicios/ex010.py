carteira = float(input('insira o valor que você possui na carteira: '))
dolar = carteira / 5.48
resultado = round(dolar, 2)

print(f'você pode comprar US${resultado}')