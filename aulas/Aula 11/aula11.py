print('\033[1;31mOlá Mundo') #\033[m no final das frases faz que a cor não vá até o final
a = 5
b = 3
nome = 'joao'
print('Os Valores são \033[1;31m{} e \033[1;31m{}'.format(a,b))

print('Olá como vai , {}{}{}'.format('\033[1;31m', nome ,'\033[m')) #Outra forma de fazer com menos código no final 