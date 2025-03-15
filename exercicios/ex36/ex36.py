casa = float(input('Qual o valor da casa: '))
sal = float(input('Qual o salário do comprador: '))
anos = int(input('Quantos anos de financiamento: '))
prestacao = casa / (anos * 12)
minimo = sal * 30 / 100

print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa , anos), end='')
print('As pretações serão de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Empréstimo pode ser Concedido')
else:
    print('Empréstimo NEGADO')
