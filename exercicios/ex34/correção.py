sala = float(input('Qual o Salário do Funcionário R$: '))
if sala <= 1250:
    novo = sala + (sala * 15 / 100)
    print('Quem Ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora'.format(sala, novo))
else:
    novx = sala + (sala * 10 / 100)
    print('Quem Ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora'.format(sala,novx))