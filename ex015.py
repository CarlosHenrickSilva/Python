'''Mostre a distância percorrida em Km por um carro, os dias pelos quais ele foi alugado,
e calcule o total a ser pago'''
# R$60,00 por dia e R$0,15 por km rodado
km = int(input('\033[1:39:40mA distância percorrida pelo carro foi de:\033[m '))
d = int(input('\033[1:39:40mPor quantos dias?\033[m '))
a = d * 60
kmrod = float(km * 0.15)
tot = a + kmrod
print('\033[7:37:40mO valor do aluguel será de: {}R${:.2f}{}'.format('\033[1:33:40m', tot, '\033[m'))
