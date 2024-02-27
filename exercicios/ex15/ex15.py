print('Informe quantos dias você ficou com o veículo')
dias = int(input(">> Dias: "))
print('Agora informe quantos KM você rodou com o veículo')
km = float(input('KM Rodados: '))
valordias = dias * 60
kmtotal = km * 0.60
totalpagar = valordias + kmtotal
print('Você irá pagar um total de {:.2f} Reais'.format(totalpagar))

