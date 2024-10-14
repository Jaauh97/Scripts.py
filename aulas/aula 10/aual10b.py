nota = float(input('Digite a nota do primeiro semestre: '))
nota1 = float(input('Digite a nota do segundo semestre: '))
m = (nota + nota1)/2


print('A sua média doi de {:.1f}'.format(m))
if m >= 10.0:
    print('Você passou , Parabéns')
else:
    print('Você está de recuperação')