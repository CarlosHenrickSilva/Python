'''Faça um programa que leie um número qualquer e leie seu fatorial'''
#usando import
#from math import factorial
#n = int(input('Digite um número: '))
#f = factorial(n)
#print('O fatorial de {} é {}'.format(n, f))
#usando for
#n = int(input('Digite um número para saber o fatorial: '))
#f = 1
#for c in range(1, n + 1):
    #f *= c
#print('O resultado de {}! é {}'.format(n, f))
#usando while
n = int(input('Digite um número para ver seu fatorial: '))
cont = n
f = 1
print('Calculando {}!'.format(n))
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f *= cont
    cont -= 1
print(f)