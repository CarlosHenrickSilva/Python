'''Calcule o aumento de salário de um funcionário. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%,
para inferiores ou iguais, 15%'''
sal = float(input('Qual é o salário do funcionário? '))
if sal <= 1200:
    novo = sal + (sal * 15/100)
else:
    novo = sal + (sal * 10/100)
print('Quem ganhava R${:.2f} passará a ganhar R${:.2f}'.format(sal, novo))


