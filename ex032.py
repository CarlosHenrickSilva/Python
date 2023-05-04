'''Mostre um ano e diga se ele é BISSEXTO ou não'''
from datetime import date
ano = int(input('Qual ano quer analizar? Digite 0 para o atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print('\033[7:32:40mO ano {} é BISSEXTO\033[m'.format(ano))
else:
    print('\033[7:31:40mO ano {} NÃO É BISSEXTO!\033[m'.format(ano))
