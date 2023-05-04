'''Crie um programa que mostre duas notas de um aluno e calcule a média'''
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média entre 7.0 ou superior: APROVADO
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
m = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f} sua média é {:.1f}'.format(nota1, nota2, m))
if 7 > m >= 5:
    print('\033[7:36:40mRECUPERAÇÃO!\033[m')
elif m < 5:
    print('\033[7:31:40mREPROVADO!\033[m')
elif m >= 7:
    print('\033[7:32:40mAPROVADO!\033[m')
