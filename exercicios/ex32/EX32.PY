from datetime import date # Biblioteca para importar datas
ano = int(input('Que ano você quer Analisar ? Coloque 0 para analisar o ano atual '))
if ano == 0:
    ano = date.today().year #importa data atual do pc , nesse exemplo ele pega o ano
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} é NÃO É BISSEXTO'.format(ano))