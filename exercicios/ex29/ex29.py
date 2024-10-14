vel = float(input('A qual velocidade você estava ?'))
if vel > 80:
    print('MULTADO !! Você excedeu o limite permitido que é de 80KM')
    multa = (vel-80)*7
    print('Você deve pagar uma multa de R$ {}'.format(multa))
print('Tenha um bom dia ! Dirija com cuidado .')