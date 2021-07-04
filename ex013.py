#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

sal = float(input('Digite o valor do seu salario: '))
desconto = (sal * 15)/100
novosal = sal + desconto
print('O valor do seu salario com aumento é: {:.2f}'.format(novosal))