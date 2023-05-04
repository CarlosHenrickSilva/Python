'''Crie uma tupla preenchida com os 20 primeiros colocados do Brasileirão, na ordem de colocação.
Depois mostre:'''
#Os 5 primeiros
#Os últimos 4 colocados
#Os times em ordem alfabética
#Em que posição está o Flamengo
times = ('Flamengo','Palmeiras','Santos','Grêmio','Cruzeiro','Corinthians','Vasco','RB Bragantino',
'Athlético','Botafogo','Atlético-PR','Bahia','São Paulo','Fluminense','Sport Recife','EC Vitória',
'Curitiba','Cuiabá','América-MG','Atlético-GO')
print('=' * 23)
print('BRASILEIRÃO ASSAÍ 2023')
print('=' * 23)
print(f'Lista de times do Brasileirão: {times}')
print('=' * 30)
print(f'Os 5 primeiros colocados são: {times[0:6]}')
print('=' * 30)
print(f'Os últimos 4 colocados são: {times[-4:]}')
print('=' * 30)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('=' * 30)
print(f'O Flamengo está na {times.index("Flamengo")+1} posição')