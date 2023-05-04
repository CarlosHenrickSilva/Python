'''Crie um programa que leie vários números inteiros pelo teclado. No final da execução mostre
a média entre todos os valores e qual foi o maior e o menor valor digitado. O programa deve perguntar
ao usuário se ele deseja continuar ou não'''
resp = 'S'
cont = soma = maior = menor = m = 0
while resp in 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar? [S/N]:')).upper().strip()[0]
m = soma / cont
print('Você digitou {} números e a média foi {}'.format(cont, m))
print('O menor número digitado foi {} e o maior foi {}'.format(menor, maior))
