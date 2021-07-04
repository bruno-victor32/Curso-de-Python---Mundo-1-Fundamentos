num = int(input('Informe um número: '))
unid = num // 1 % 10
deze = num // 10 % 10
cente = num // 100 % 10
milha = num // 1000 % 10
print('Unidade {}'.format(unid))
print('Dezena {}'.format(deze))
print('Centena {}'.format(cente))
print('Milhar {}'.format(milha))