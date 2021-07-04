from random import choice
n1 = int(input('Qual número que você acha que vai ser sorteado '))
lista = [0, 1, 2, 3, 4, 5]
print('\033[4;30;45mPROCESSANDO...\033[m')
escolhido = choice(lista)
if n1 == escolhido:
        print('O numero escolhido foi \033[1;32m{} \033[m .\033[4;31;40mParabéns você ACERTOU\033[m'.format(escolhido))
else :
        print('O numero escolhido foi \033[7;30;43m{} \033[m.\033[7;30;43mInfelizmente você não ACERTOU\033[m'.format(escolhido))