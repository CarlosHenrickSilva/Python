'''Leia o peso e altura de uma pessoa e calcule seu IMC'''
# Abaixo de 18.5: abaixo do peso
# Entre 18.5 e 25: peso ideal
# 25 até 30: sobrepeso
# 30 até 40: obesidade
# Acima de 40: obesidade mórbida
peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso /(altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal')
elif 25 <= imc < 30:
    print('Você está em sobrepeso')
elif 30 <= imc < 40:
    print('VocÊ está em obesidade')
elif imc >= 40:
    print('Você está em obesidade mórbida. Cuidado!')