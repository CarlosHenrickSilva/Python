'''Digite o seu nome e mostre em maiúsculo, minúsculo, e a quantidade de letras do primeiro nome e o total'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculo é: {}'.format((nome.lower())))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))