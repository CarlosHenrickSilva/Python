'''Digite seu nome completo, se tiver ''SILVA'', true, se não, false'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem SILVA? {}'.format('silva' in nome.lower()))
