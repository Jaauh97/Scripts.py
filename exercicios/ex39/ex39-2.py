from datetime import date

ano = int(input('Em que ano vc nasceu :'))
atual =  date.today().year
idade = atual - ano

if idade > 18:
    saldo = idade - 18
    print('Voce deveria ter se alistado há {} anos'.format(saldo))
    prev = atual - saldo
    print('Seu alistamento deveria ter sido em {}'.format(prev))

elif idade == 18:
    print('Voce já pode se alistar')

else:
    saldo = 18 - idade
    print('Ainda faltam {} anos para voce se alistar '.format(saldo))
    prev = atual + saldo
    print('Seu alistamento será em {}'.format(prev))

# adicionei a variavel saldo para saber quanto tempo falta para se alistar
# foi so fazer a idade - 18 ou + 18

