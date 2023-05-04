'''Pergunte o valor da casa, o salário do comprador e em quantos anos ele irá pagar. A prestação mensal
não pode exceder 30% do salário do comprador ou então o empréstimo será negado.'''
casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual é o seu salário? '))
anos = int(input('Quantos anos de financiamento? '))
prest = casa/(anos * 12)
min = sal * (30/100)
print('Para pagar uma casa de R${:.2f} em {} anos. '.format(casa, anos), end='')
print('A prestação será de R${:.2f}'.format(prest))
if prest <= min:
    print('\033[7:32:40mEmpréstimo pode ser concedido!\033[m')
else:
    print('\033[7:31:40mEmpréstimo negado!\033[m')

