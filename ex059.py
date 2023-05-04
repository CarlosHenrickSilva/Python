'''Crie um programa que leie dois valores e mostre um menu:'''
#[ 1 ] somar
#[ 2 ] mutiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
option = int(input('Qual é a sua opção? '))
if option == 1:
    soma = n1 + n2
    print('A soma entre {} e {} é igual a: {}'.format(n1, n2, soma))
elif option == 2:
    mult = n1 * n2
    print('A multiplicação entre {} e {} é igual a: {}'.format(n1, n2, mult))
elif option == 3:
    if n1 > n2:
        maior = n1
    else:
        maior = n2
        print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
while option == 4:
    print('Digite novos números:')
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    print('''[ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    option = int(input('Qual é a sua opção? '))
    if option == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual a: {}'.format(n1, n2, soma))
    elif option == 2:
        mult = n1 * n2
        print('A multiplicação entre {} e {} é igual a: {}'.format(n1, n2, mult))
    elif option == 3:
       if n1 > n2:
            maior = n1
       else:
            maior = n2
            print('O maior número entre {} e {} é {}'. format(n1, n2, maior))
if option == 5:
    print('Você saiu')