from random import randint
from time import sleep

num1 = randint(0,5)
#print(num1)
print('=-='*20)
print('Jogo da Adivinhação !! ')
print('=-='*20)

numusu = int(input('Vou pensar em número entre 0 e 5 , tente advinhar:  '))
#jogador tenta advinhar
print('PENSANDO...')
sleep(2)
print('=-='*20)

if numusu == num1:
    print('Parabéns Você Acertoou')
    print('Eu pensei no {}'.format(num1))
else:
    print('Você errou, tente outra vez !!')
    print('O Numero que eu pensei foi {}'.format(num1))
