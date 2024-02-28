from math import trunc
import math
print('='*45)
print('Digite um número real (EX: 1.5 , 2.0 , 9.2) e veja sua versao inteira:')
num1 = float(input('>>>Digite aqui: '))
num2 = math.floor(num1)
num3 = math.ceil(num1)
print('Versao real de {} é {} ou {}'.format(num1, num2, num3))
print('='*45)


print('='*45)
print('Digite um número real (EX: 1.5 , 2.9, 9.1) e veja sua porção inteira.')
num2 = float(input('>>> Digite aqui: '))
print('A porção inteira de {} é {} '.format(num1, trunc(num2)))
print('='*45)


num3 = float(input('Digite um número real e veja sua porção inteira: '))
print('A porção inteira de {} é igual a {}'.format(num3, int(num3)))