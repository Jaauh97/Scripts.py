prim = int(input('Qual o primeiro termo: '))
raz = int(input('Qual a razão: '))
dec = prim + (10 - 1) * raz #Décimo termo é assim que calcula , eu faço uma progressão de número até o 10.
for c in range(prim, dec, raz):
    print('{}'.format(c),end=' -> ')
print('ACABOU')    
    