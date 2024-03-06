nota1 = float(input('Digite Sua Nota: '))
nota2 = float(input('Digite Sua 2 Nota: '))
r = (nota1 + nota2)/2
print('Sua Nota final foi de {}.'.format(r))
if r >=6.0:
    print('Voce passou de ano. ')
else:
    print('Voce está de recuperação .')