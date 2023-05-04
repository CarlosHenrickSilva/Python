'''Refaça o ex035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado'''
# Equilátero : todos os lados iguais
# Isóscles : dois lados iguais
# Escaleno : todos os lados diferentes
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 + r2 >= r3 and r1 + r3 >= r2 and r2 + r3 >= r1:
    print('Os segmentos acima podem formar um triângulo!')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('\033[7:31:40mOs segmentos acima NÃO podem formar um triângulo!\033[m')