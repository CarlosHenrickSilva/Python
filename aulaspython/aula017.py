lista = ['cachorro', 'criança', 'boi', 'rapariga']
lista[2] = 'cavalo'
lista.append('urubu')
lista.insert(0, 'jegue')
del lista[2]
lista.sort()
lista.remove('rapariga')
print(lista)
print(f'Essa lista tem {len(lista)} elementos')