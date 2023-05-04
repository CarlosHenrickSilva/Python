'''Faça um programa que leie o sexo e uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a
digitação correta até ter um valor correto'''
s = str(input('Digite seu sexo: [F/M] ')).upper().strip()[0]
while s not in 'F/M':
    s = str(input('Sexo inválido, digite novamente: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(s))

