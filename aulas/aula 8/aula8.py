#from math import sqrt
#from math import sqrt, floor

import math
num = int(input('Digite um nuemro e veja sau raiz quadrada: '))
raiz = math.sqrt(num)
#raiz = sqrt(num)
#print('A raiz de {} é igual a {} ', format(num, floor(raiz)))
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

#quando colocar a biblioteca td,  da pra usar tds os math. (Ex: math.sqrt)

#quando chamar algo especifico so da pra chamar a biblioteca que foi pega (EX: se chamar from math import sqrt so pode
#sqrt(num) )

#pode se chamar bibliotecas em especifico basta colocar virgula (EX: from math import sqrt, floor )

