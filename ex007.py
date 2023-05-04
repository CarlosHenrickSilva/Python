'''Mostre a média entre duas notas de um aluno'''
n1 = float(input('\033[37:40mPrimeira nota:\033[m '))
n2 = float(input('\033[37:40mSegunda nota:\033[m '))
m = (n1 + n2) /2
print('\033[7:32:40mA sua média é {}\033[m'.format(m))