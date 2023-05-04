'''Digite um número e mostre seu dobro, seu triplo e sua raizQ'''
n = int(input('\033[7:36:40mDigite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('Você digitou o número {}: seu dobro é {}, seu triplo é {} e sua raizQ é {}\033[m'.format(n, d, t, r))