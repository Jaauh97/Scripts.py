import random

num1 = random.randint(0,5)
#print(num1)
print('='*45)
print('Jogo da Adivinhação ')
numusu = int(input('Digite um Numero entre 0 e 5 e veja se você acertou: '))

if numusu == num1:
    print('Parabéns Você Acertoou')
else:
    print('Você errou, tente outra vez !!')
