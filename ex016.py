'''Digite um número e mostre sua parte inteira'''
from math import trunc
num = float(input('\033[4:30mDigite um número:\033[m '))
print('O valor digitado foi {}{}{} e sua parte inteira é {}{}{}'.format('\033[4:40m', num, '\033[m','\033[4:40m', trunc(num), '\033[m'))