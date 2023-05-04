'''Digite o nome da cidade em que nasceu, se começar com ''SANTO'' escreva VERDADEIRO, se não, FALSO'''
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')

