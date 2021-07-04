import math
km = float(input('Digite a distância pretendida na viagem em km: '))
if km <= 200 :
    res = km * 0.50
    print('O valor da passagem da viagem mais curta é R${:.2f}'.format(res))
else:
    res1 = km * 0.45
    print('O valor da passagem da viagem mais longa é R${:.2f}'.format(res1))