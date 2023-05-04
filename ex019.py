'''Escreva 4 nomes e sorteie 1'''
import random
n1 = str(input('\033[1:39:40mPrimeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: \033[m'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('\033[7:40mO aluno escolhido foi: {}{}{}'.format('\033[7:32:40m', escolhido, '\033[m'))