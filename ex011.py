'''Mostre a largura e a altura de uma parede e calcule a área a ser pintada'''
l = float(input('\033[2:30:42mQual a largura da parede? '))
a = float(input('Qual a altura da parede? '))
area = float(l * a)
tot = float(area/2)
print('A quantidade de tinta necessária para pintar a perede é de {}L\033[m'.format(tot))

