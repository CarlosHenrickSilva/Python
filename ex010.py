'''Converta R$ em US$'''
#Preço do dólar: R$5,28 (29/12/2022)
rs = float(input('\033[1:39:40mQuantos reais você tem?\033[m '))
dol = float(rs/5.28)
print('\033[1:39:40mCom {}R${:.2f}{}\033[1:39:40m você pode comprar {}US${:.2f}{}'.format('\033[7:36:40m', rs, '\033[m',
'\033[7:32:40m', dol, '\033[m'))