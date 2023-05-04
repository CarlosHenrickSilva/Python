'''Digite um número e mostre se antecessor e seu sucessor'''
n = int(input('\033[7:34:40mDigite um número:\033[m '))
ant = n - 1
suc = n + 1
print('\033[36:40mVocê digitou o número {}, seu antecessor é {}{}{}\033[36:40m e seu sucessor é {}{}{}\033[m'.format(n, '\033[31m', ant, '\033[m', '\033[32m', suc, '\033[m'))