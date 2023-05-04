'''Mostre a distância da viagem e calcule o preço a ser pago pela passagem, cobrando R$0,50 por Km pela passagem
para viagens até 200km e R$0,45 para viagens mais longas'''
km = int(input('Qual a distância da viagem? '))
print('Você está prestes a fazer uma viagem de {}Km'.format(km))
if km <= 200:
    psg = km * 0.50
else:
    psg = km * 0.45
print('O valor da passagem é de R${:.2f}'.format(psg))
