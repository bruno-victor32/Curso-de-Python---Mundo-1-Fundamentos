vel = float(input('Digite a velocidade do veiculo em km/h: '))
if vel > 80:
    print('Você foi multado devido a está acima do limite de 80 km/h')
    mul = (vel - 80) * 7
    print('A multa vai custar R${:.2f}'.format(mul))
else:
    print('Você está andando na velocidade correta')