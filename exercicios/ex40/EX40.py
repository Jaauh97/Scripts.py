nota1 = float(input('Primeira Nota: '))
nota2 = float(input('Segunda Nota: '))
notaf = (nota1 + nota2) / 2


if notaf < 5.0:
    print('Sua nota foi {:.1f}.Você foi REPROVADO !!'.format(notaf))
elif notaf == 5.0 or notaf <= 6.9 :
    print('Sua nota foi {}. Você está na média .'.format(notaf))
elif notaf >= 7.0:
   print('Sua nota foi {:.1f}. Você foi APROVADO !!'.format(notaf))