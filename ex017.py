'''Calcule a hipotenusa'''
from math import hypot
co = float(input('\033[7:40mComprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('\033[1:32:40mA hipotenusa vai medir {:.2f}\033[m'.format(hi))