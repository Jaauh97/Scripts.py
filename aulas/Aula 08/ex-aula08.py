import math
import random

print('Veja a raiz quadrada e a tabuada de número aleatório')
num1 = random.randint(1, 50)
num2 = math.sqrt(num1)
print('Raiz quadrada de {} é igual a {:.2f}'.format(num1, num2))
print('A tabuada de Multiplicação do {} :'.format(num1))
print('{} x 1  =  {}'.format(num1,num1*1))
print('{} x 2  =  {}'.format(num1,num1*2))
print('{} x 3  =  {}'.format(num1,num1*3))
print('{} x 4  =  {}'.format(num1,num1*4))
print('{} x 5  =  {}'.format(num1,num1*5))
print('{} x 6  =  {}'.format(num1,num1*6))
print('{} x 7  =  {}'.format(num1,num1*7))
print('{} x 8  =  {}'.format(num1,num1*8))
print('{} x 9  =  {}'.format(num1,num1*9))
print('{} x 10  =  {}'.format(num1,num1*10))