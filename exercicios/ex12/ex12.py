print('Digitre o valor cheio do produto e descubra seu valor com desconto de 5%')
desc = float(input('Digite o Valor: '))
desc2 = (desc/100) * 5
descfinal = desc - desc2
print('O valor de {} com 5% de desconto fica {} Reais, foram descontatos um total de {} Reais'.format(desc, descfinal, desc2))