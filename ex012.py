'''Mostre o desconto de 5% em um determinado produto'''
v = float(input('\033[1:39:40mQual o valor do produto?\033[m '))
d = 5 / 100
vf = v - (v * d)
print('\033[7:40mCom 5% de desconto o seu produto de {}R${:.2f}{}\033[7:40m passa a ser {}R${:.2f}{}'.format('\033[7:36:40m', v,
'\033[m', '\033[7:32:40m', vf, '\033[m'))
