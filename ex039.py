'''Leia a data de nascimento de um jovem e diga se ele ainda vai se alistar, se ele deve se alistar imediatamente,
ou já passou do prazo de alistamento'''
from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} e terá {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você deve se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para seu alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))