'''Calcule o valor de um produto, considerando o seu preço normal e condição de pagamento'''
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
price = float(input('Preço das compras: '))
print('''Formas de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
option = int(input('Qual opção? '))
if option == 1:
    total = price - (price * 10/100)
elif option == 2:
    total = price - (price * 5/100)
elif option == 3:
    total = price
    parcela = total / 2
elif option == 4:
    total = price + (price * 20/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}X de R${:.2f} com juros'.format(totparc, parcela))
else:
    total = 0
    print('Opção inváli')
    print('Opção inválida! Tente novamente.')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(price, total))

