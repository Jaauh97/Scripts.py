for c in range(0 , 3):
    print('OI')   # Estrutura básica de repetição com for
                  #no range sempre vai entregar um número a menos do quer foi colocado no ()
print('FIM')


for c in range(0, 3+1): # Estrutura básica de repetição com for, para números
    print(c)

print('FIM')



for c in range(0 ,9 , 2):
     print(c) #adiciona um número após a vírgula para que a contagem possa pular


n = int(input('Digite um número: '))
for c in range(0, n):
    print(c)


i = int(input('Início: '))
f = int(input('Final: '))
p = int(input('Passo: '))
for c in range(i , f , p):
    print(c)



for c in range(0, 3):
    j = int(input('Digite um número: ')) #loop para pedir 'Informação'


s = 0
for c in range(0, 4):
    p = int(input('Digite um valor: '))
    s = s + p
    print(s)  #Forma básica de somar valores com for


