print('-'*45)
print('>>> Digite seu salário atual e veja seu novo salário com reajuste de 15% .')
sal = float(input('Salário Atual: '))
sal2 = (sal/100) * 15
salatual = sal + sal2
print('-'*45)
print('Seu Salário irá para {:.2f} Reais , houve um acréscimo de {:.2f} R$'.format(salatual, sal2))
print('-'*45)