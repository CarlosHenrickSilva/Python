'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em um tupla. No final, mostre:'''
#Quantas vezes apareceu o valor 9
#Em que posição foi  digitado o primeiro valor 3
#Quais foram os números pares
num = tuple(int(input('Digite valores '))for c in range(1, 5))
print(f'Você digitou os valores {num}')
print(f'Você digitou o valor 9 {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares são:')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
else:
    print('Não há valor par')


