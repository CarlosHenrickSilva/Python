'''Mostre o nome de 4 alunos e sorteie a ordem de apresentação'''
from random import shuffle
a1 = str(input('\033[1:34:41mPrimeiro aluno: '))
a2 = str(input('\033[30:42mSegundo aluno: \033[m'))
a3 = str(input('\033[4:36mTerceiro aluno: '))
a4 = str(input('\033[7:30:41mQuarto aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('\033[1:39:40mA ordem será:\033[m {}'.format(lista))

