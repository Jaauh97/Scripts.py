city = str(input('Nome de uma cidade: ')).strip()
print('Essa cidade possui a palavra SANTO em seu nome:','santo' in city)



#correção
cid = str(input('Digite o nome de uma cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')
