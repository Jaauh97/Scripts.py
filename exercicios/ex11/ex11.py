print('-'*45)
print('Digite a Largura e a Altura de sua parede para calcular a Área')
larg = float(input('>>> Largura: '))
alt = float(input('>>> Altura: '))
area = larg * alt
print('Sua parede é de {} x {} e sua área e de {}.'.format(larg, alt, area))
tinta = area / 2
print('Você Irá Precisar de {} Litros de tinta por metro quadrado. '.format(tinta))