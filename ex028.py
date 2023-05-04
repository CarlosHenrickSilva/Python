'''Faça o computador sortear um número de 0 a 5 e tente adivinhar'''
from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar!')
print('-=-' * 20)
jogador = int(input('Digite um número: '))
print('PROCESSANDO...')
sleep(1.5)
if jogador == computador:
    print('\033[7:32:40mVocê venceu!\033[m')
else:
    print('\033[7:31:40mVocê perdeu! Pensei no número {} haha!\033[m'.format(computador))




