'''Crie uma contagem regressiva de 10 até 0 com intervalo entre cada número'''
from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('Its over!!!')
    