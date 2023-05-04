'''Crie um programa que simula o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.'''
#Considere que o caixa só possui cédulas de R$50, R$20, R$10 e RS1
print('=' * 20)
print('{:^20}'.format('MAVERICK BANK'))
print('=' * 20)
saque = int(input('Quanto você quer sacar? '))
total = saque
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Todal de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 20)
print('Volte sempre ao MAVERICK BANK! Tenha um ótimo dia!')