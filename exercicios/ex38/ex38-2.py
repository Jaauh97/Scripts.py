num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

if num1 > num2:
    print('{} é maior que {} entao o primeiro numero é maior '.format(num1, num2))
elif num1 < num2:
    print('{} é maior que {} entao o segundo numero é maior'.format(num2, num1))
else:
    print('Nao existe valor maior. Os dois sao iguais')