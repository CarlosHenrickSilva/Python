'''Leia algo no teclado e mostre seu tipo primitvo e todas as informações sobre ele'''
a = input('\033[32:40mDigite algo:\033[m ')
print('\033[31mO tipo primitivo desse valor é: ', type(a))
print('\033[32mSó tem espaços? ', a.isspace())
print('\033[33mÉ um número? ', a.isnumeric())
print('\033[34mÉ alfabético? ', a.isalpha())
print('\033[35mÉ numérico? ', a.isnumeric())
print('\033[36mÉ MAIÚSCULO? ', a.isupper())
print('\033[37mé minúsculo? ', a.islower())
print('\033[30mEstá capitalizado? \033[m', a.istitle())