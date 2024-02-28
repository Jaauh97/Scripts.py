import math
print('='*45)
print('Digite um número real (EX: 1.5 , 2.0 , 9.2) e veja sua versao inteira:')
num1 = float(input('>>>Digite aqui: '))
num2 = math.floor(num1)
num3 = math.ceil(num1)
print('Versao real de {} é {} ou {}'.format(num1, num2, num3))
print('='*45)
