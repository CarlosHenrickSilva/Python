'''Melhore o jogo do ex028, onde o computador vai "pensar" em um número entre 0 e 10. o jogador deverá tentar
até acertar, e mostre quantas tentativas foram feitas'''
from random import randint
print('Vou pensar em um número de 0 a 10, tente adivinhar!')
computador = randint(0, 10)
cont = 0
acertou = False
while not acertou:
    jogador = int(input('Tente acertar: '))
    cont +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...tente novamente: ')
        elif jogador > computador:
            print('Menos...tente novamente: ')
print('\033[7:32:40mV \ocê acertou com {} palpites\033[m'.format(cont))