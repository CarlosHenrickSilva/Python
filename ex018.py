'''Digite um ângulo e mostre seu SENO, COSSENO e TANGENTE'''
from math import radians, sin, cos, tan
ang = float(input('\033[1:39:40mDigite o ângulo que você deseja:\033[m '))
seno = sin(radians(ang))
print('\033[1:35:40mO ângulo de {} tem SENO de {:.2f}\033[m'.format(ang, seno))
cosseno = cos(radians(ang))
print('\033[1:36:40mO ângulo de {} tem o COSSENO de {:.2f}\033[m'.format(ang, cosseno))
tangente = tan(radians(ang))
print('\033[1:34:40mO ângulo de {} tem TANGENTE de {:.2f}\033[m'.format(ang, tangente))