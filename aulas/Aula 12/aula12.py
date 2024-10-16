nome = str(input('\033[31mQual seu nome ? '))
if nome == 'joao' or nome == 'mateus':
    print('\033[1;31mQue nome bonito !!')
elif nome == 'pedro' or nome == 'ana' or nome == 'maria':
    print('\033[1;31mSeu nome é bem comum no brasil .') 
elif nome in 'Ana claudia jorge ': # in pode ser usado no lugar do ==
    print('Belo nome feminino')       
else:
    print('Seu nome é bem normal')
print('\033[1;34mTenha um bom dia, {}.'.format(nome)) 