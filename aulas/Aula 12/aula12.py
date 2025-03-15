nome = str(input('Qual seu nome ? '))
if nome == 'Joao'or nome == 'joao':
    print('Que nome bonito !')
elif nome == 'pedro' or nome == 'Pedro':
    print('Que nome legal, {}'.format(nome))

elif nome == 'Maria' or nome == 'Jose' or nome == 'Ana' :
    print('Seu nome é bem popular no brasil.')
    
elif nome in 'Beatriz Claudia': #Ultilize o in ao inves de == para usar mais de uma opcao de nome 
    print('Que belo nome feminino. ')
    
else:
    print('Seu nome é tão normal')
print('Tenha um bom dia, {}!'.format(nome)) # esse print esta no canto pois ele será executado independente da condicao