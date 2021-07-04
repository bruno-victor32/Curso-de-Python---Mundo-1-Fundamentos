n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisaoint = n1 // n2
potencia = n1 ** n2
print('A soma é {} , \no produto é {} e a divisão é {:.3f}'.format(soma, multiplicacao, divisao), end=' ')
print('Divisão inteira {} e potencia {}'.format(divisaoint, potencia))