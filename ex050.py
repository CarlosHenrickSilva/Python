'''Leia 6 números inteiros e mostre a soma daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o'''
soma = 0
cont = 0
for c in range (1, 7):
    num  = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você informou {} numeros pares e a soma foi {}'.format(cont, soma))
