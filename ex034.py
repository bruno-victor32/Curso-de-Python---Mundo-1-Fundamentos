n1 = float(input('Digite o valor do salário atual: '))
if n1 > 1250:
    res = (n1*10)/100
    resfinal =  n1 + res
    print('O senhor(a) terá um aumento de R${:.2f} e salario final de R${:.2f}'.format(res, resfinal))
else:
    res1 = (n1*15)/100
    resfinal1 = n1 + res1
    print('O senhor(a) terá um aumento de R${:.2f} e salario final de R${:.2f}'.format(res1, resfinal1))
