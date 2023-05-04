'''Digite um comprimento e mostre em metros, centímetros e milímetros'''
m = float(input('\033[33mQuantos metros?\033[m '))
c = float(m * 100)
mm = float(m * 1000)
print('Em {}{}{}m, tem {}{}{}cm e {}{}{}mm'.format('\033[33m', m, '\033[m', '\033[34m', c, '\033[m', '\033[32m', mm, '\033[m'))