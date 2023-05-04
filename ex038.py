'''Escreva um programa que leie os números inteiros e compare-os, mostrando na tela uma mensagem'''
# O 1° valor é maior
# O 2° valor é maior
# Não existe valor maior, os dois são iguais
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O primeiro valor é maior!')
if n2 > n1:
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais')