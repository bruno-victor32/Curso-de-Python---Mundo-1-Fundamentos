preco = float(input('Digite o valor do produto: '))
desconto = (preco * 5) / 100
preconovo = preco - desconto
print('O valor com desconto e {:.0f} reais'. format(desconto))
print('O preço com desconto incluido e {:.2f} reais'.format(preconovo))