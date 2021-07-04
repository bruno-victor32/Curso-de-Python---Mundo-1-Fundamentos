ano = int(input('Digite um ano para verificar si e bissexto:'))
res = ano % 4
res1 = ano % 100
res2 = ano % 400
if res == 0 and res1 != 0 or res2 == 0:
    print('O ano {}  e bissexto'.format(ano))
else:
    print('O ano {} não e bissexto'.format(ano))