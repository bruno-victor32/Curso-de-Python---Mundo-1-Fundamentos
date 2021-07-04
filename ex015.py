km = float(input('Quantidade de KM percorridos? '))
dia = int(input('Quantidade de dias alugados? '))
Qtdkm = km * 0.15
Qtddia = dia * 60
resfinal = Qtdkm + Qtddia
print('O total a pagar é de R${:.2f}'.format(resfinal))

