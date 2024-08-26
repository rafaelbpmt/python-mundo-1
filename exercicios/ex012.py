produto = float(input('digite o valor do produto: '))
porcentagemDesconto = 5.0
desconto = produto * (5.0 / 100.0)
final = produto - desconto

print(f'produto com desconto aplicado: R${final}')
