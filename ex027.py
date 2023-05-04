'''Digite seu nome completo e mostre seu primeiro e último nome'''
nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
print('\033[7:32:40mMuito prazer em te conhecer!\033[m')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))