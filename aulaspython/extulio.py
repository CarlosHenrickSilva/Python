'''Digite o nome de duas pessoas e peça duas notas, mostre e média e a idade deles'''
for c in range(1, 3):
    aluno = input('Digite seu nome: ').strip().title()
    print('Olá {}!'.format(aluno))
    idade = int(input('Qual a sua idade? '))
    if idade >= 18:
        print('Você tem {} anos e portanto, é maior de idade'.format(idade))
    else:
        print('Você tem {} anos e portanto, é menor de idade'.format(idade))
    n1 = int(input('Primeira nota: '))
    n2 = int(input('Segunda nota: '))
    m = (n1 + n2)/2
    print(f'Sua media foi: ',m)
    if m >= 6:
        print('Parabéns, você foi aprovado!')
    else:
        print('Você não conseguiu atingir a média, se esforce mais, animal')
    print('Tá liberado,')         