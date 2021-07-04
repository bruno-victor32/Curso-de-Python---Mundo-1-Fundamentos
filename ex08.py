#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

metros = float(input('Digite o valor a ser convertido em metros: '))
cm = metros * 100
mm = metros * 1000
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
print('O valor em metros é {}m, em cm {:.0f}cm, em km {}km, em hm {}hm, em dam {:.0f}dam, em dm {:.0f}dm e em mm {:.0f}mm'.format(metros, cm,km,hm,dam,dm, mm) )
