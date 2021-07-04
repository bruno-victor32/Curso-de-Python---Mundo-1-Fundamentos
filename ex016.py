#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira

from math import trunc
num = float(input('Digite um número: '))
inteiro = trunc(num)
print('O número {:.3f} tem a parte inteira {}'.format(num, inteiro))