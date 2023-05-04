'''Crie um programa que leie o nome e o preço de vários produtos. O programa deverá
perguntar se o usuário vai continuar. No final mostre: '''
#Qual é o total gasto na compra;
#Quantos produtos custam mais de R$ 1.000,00;
#Qual é o produto mais barato.
print('MAVERICK STORE')
print(f'==' * 10)
tot = mais = menor = cont = 0
barato = ' '
resp = 'S'
while resp in 'S':
    nome = str(input('Qual o nome do produto? '))
    preço = float(input('Qual o preço do produto? '))
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    cont += 1
    tot += preço
    if preço > 1000:
        mais += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = nome
print(f'o total gasto foi de R${tot:.2f}')
print(f'{mais} produtos custaram mais de R$ 1.000,00')
print(f'O produto mais barato foi {nome} e o preço foi R${menor}')
