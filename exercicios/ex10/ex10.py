print('Digite o valor em Real que deseja converter em Dolar')
reais = float(input('Valor: '))
print('Com {}R$, você irá comprar {:.2f} Dolares.'.format(reais, (reais*4.98)))