'''Digite um número e mostre se ele é PAR ou ÍMPAR'''
n = int(input('Digite um número: '))
resp = n % 2
if resp == 0:
    print('O número {} é PAR!'.format(n))
else:
    print('O número {} é ÍMPAR!'.format(n))

