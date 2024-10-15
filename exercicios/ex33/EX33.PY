a = int(input('Digite o Primeiro Número: ')) #pedindo os números
b = int(input('Digite o Segundo Número: '))
c = int(input('Digite o Terceiro Número: '))

#verificando quem é o menor
if a < b and a < c:
 menor =  a
if b < c and b < a:
 menor = b
if c < a and c < b:
 menor = c 

#vericando quem é o maior número 
if a > b and a > c:
 maior =  a
if b > c and b > a:
 maior = b
if c > a and c > b:
 maior = c  
 
#mostrando o resultado final
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))