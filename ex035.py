#Desenvolva u programa que leia o comprimento de três retas e diga ao usuário se els podem ou não formar
#um triângulo.
r1 = float(input('\033[1:39:40mPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento:\033[m '))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('\033[7:32:40mÉ possivel formar um triângulo!\033[m')
else:
    print('\033[7:31:40mNão é possivel formar um triângulo!\033[m')