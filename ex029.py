'''Mostre a velocidade do veículo se exceder o limite de 80km/h, MULTADO.'''
# A multa irá custar R$ 7,00 por cada km acima do limite
vel = int(input('Qual a velocidade do veículo? '))
if vel > 80:
    multa = (vel - 80) * 7
    print('\033[7:31:40mVocê foi multado em R${:.2f}. Por favor, dirija com segurança!\033[m'.format(multa))
else:
    print('\033[7:32:40mVocê está dentro do limite de velocidade permitido. Tenha um bom dia!\033[m')
