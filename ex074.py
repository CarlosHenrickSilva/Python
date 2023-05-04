'''Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem
de números gerados e também indique o menor e o maior valor que estão na tupla'''
from random import randint
números = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
for n in números:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(números)} e o menor foi {min(números)}')
