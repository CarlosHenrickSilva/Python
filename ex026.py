'''Digite uma frase e mostre quantas vezes aparece a letra A e em que posição ela aparece pela
primeira vez e pela última vez'''
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra "A" apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra "A" apareceu na posição {}'.format((frase.rfind('A')+1)))
