# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar

n = float(input('Digite o valor a ser convertido em dolares: R$'))
dolares = 0.20
n1 = n * dolares
print('Com R${:.2f} você pode comprar atualmente US${:.2f} dolares'.format(n, n1))