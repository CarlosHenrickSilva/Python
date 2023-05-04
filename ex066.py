'''Crie um programa que leie vários números inteiros. O programa só vai parar quando o usuário digitar 999,
que é a condição de parada. No final, mostre quantos números foram digitados, e qual foi a soma entre eles
(desconsiderando o flag).'''
num = soma = cont = 0
while True:
    num = int(input('Digite um valor(999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Você digitou {cont} números e a soma deles é igual a {soma}')





