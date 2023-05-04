'''Leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade'''
# até 9 anos: MIRIM
# até 14 anos: INFANTIL
# até 19 anos: JÚNIOR
# até 25 anos: SÊNIOR
# acima: Master
from datetime import date
atual = date.today().year
nasc = int(input('Ano d nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Cassificação: MASTER')

