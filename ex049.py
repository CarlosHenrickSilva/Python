'''Refaça o ex009 mostrando a tabuada utilizando o laço for'''
num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))