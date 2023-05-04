'''Leia uma frase e diga' se ela é um palíndromo'''
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ' '.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('\033[7:32:40mTemos um palindromo!\033[m')
else:
    print('\033[7:31:40mA frase digitada não é um palíndromo!\033[m')
