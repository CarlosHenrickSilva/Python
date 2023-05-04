'''Leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão'''
primeiro = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dec = primeiro +(10 -1) * raz
for c in range(primeiro, dec + raz, raz):
    print('{}'.format(c), end=' ')
print('Acabou')
    