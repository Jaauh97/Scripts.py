from datetime import date

ano = int(input('Qual seu ano nascimento ? '))
atual =  date.today().year
alist = atual - ano

if alist < 18 :
    print('Você tem {} anos '.format(alist))
    print('Não está na hora de alistar')

elif alist == 18:
    print('Você tem {} anos'.format(alist))
    print('Você deve se alistar')

else:
    print('Você tem {} anos '.format(alist))
    print('Você já devia ter se alistado ')