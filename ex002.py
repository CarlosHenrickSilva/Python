'''Digite seu nome e escreva uma mensagem de boas vindas.'''
nome = input('\033[1:32mQual é o seu nome? \033[m')
print('\033[7:32:40mSeja bem vindo {}{}{}\033[7:32:40m!\033[m'.format('\033[1:36:40m', nome, '\033[m'))