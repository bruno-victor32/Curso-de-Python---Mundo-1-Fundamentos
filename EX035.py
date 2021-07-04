n1 = float(input('Digite o primeiro valor de um lado do triangulo: '))
n2 = float(input('Digite o segundo valor de um lado do triangulo: '))
n3 = float(input('Digite o terceiro valor de um lado do triangulo: '))
res =  (n1 + n2) > n3
res1 = (n2 + n3) > n1
res2 = (n1 + n3) > n2
if res and res1 and res2:
    print('E possivel formar um triangulo')
else:
    print('Não e possivel formar um triangulo')