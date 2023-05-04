'''Crie um programa que leie a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:'''
#Quantas pessoas tem mais de 18 anos;
#Quantos homens foram cadastrados;
#Quantas mulheres tem menos de 20 anos.
resp = 'S'
contidade = contsexo = contmulher = 0
while resp in 'S':
    print(f'CADASTRE UMA PESSOA')
    nome = str(input('Qual é o seu nome? '))
    idade = int(input('Qual é a sua idade? '))
    sexo = str(input('Qual o seu sexo? [M/F]')).upper().strip()[0]
    print(f'Seu nome é {nome} você tem {idade} anos e seu sexo é {sexo}')
    resp = str(input('Deseja continuar? [S/N]:')).upper().strip()[0]
    if idade > 18:
        contidade += 1
    if sexo == 'M':
        contsexo += 1
    if sexo == 'F' and idade < 20:
        contmulher += 1
    print(f'-' * 20)
print(f'Você cadastrou {contidade} pessoas com mais de 18 anos, {contsexo} homens no total e {contmulher} mulheres com menos de 20 anos')
print(f'Fim da operação!')