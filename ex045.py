'''Crie o jogo JO KEN PO'''
from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas ações
[ 0 ] pedra
[ 1 ] papel
[ 2 ] tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('O computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador venceu!')
    elif jogador == 2:
        print('Computador venceu')
    else:
        print('Jogada inválida!')
elif computador == 1:
    if jogador == 0:
        print('Computador venceu')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Jogador venceu')
    else:
        print('Jogada inválida!')
elif computador == 2:
    if jogador == 0:
        print('Jogador vence')
    elif jogador == 1:
        print('Computador vence')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada inválida')
        