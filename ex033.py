'''Digite 3 números e mostre o maior e o menor'''
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n2 and n3 > n1:
    maior = n3
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('\033[7:37:40mO menor número digitado foi {}\033[m'.format(menor))
print('\033[7:34:40mO maior número digitado foi {}\033[m'.format(maior))
