casa = float(input('Qual o valor da casa: '))
sal = float(input('Qual o salário do comprador: '))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = sal * 30 / 100


print('Para pagar uma casa de R${} em {} anos'.format(casa , anos))
print('As pretações seram de R${}'.format(prestacao))

if prestacao <= minimo:
    print('')