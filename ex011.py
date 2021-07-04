#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m^2

altura = float(input('Digite a altura em metros: '))
largura = float(input('Digite a largura em metros: '))
area = largura * altura
qtdtinta = area / 2
print('A área é {}m², e vamos precisar de {}L de tintas'.format(area, qtdtinta))
