'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
lista = ('Caderno', 5.99,
         'Lápis', 0.99,
         'Caneta', 1.99,
         'Mochila', 49.99,
         'Borracha', 0.99,
         'Tesoura', 2.99)
print('-' * 37)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-' * 37)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>5.2f}')
print('-' * 37)