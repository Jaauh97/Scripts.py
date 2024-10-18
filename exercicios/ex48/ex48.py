soma = 0 #Declarei uma variavel igual a zero
cont = 0

for c in range(1, 501, 2) :#dessa forma ele já me mostra todos os números impar
    if c % 3 == 0: #Dessaa forma eu faço com que apareçam somente os números que são % por 3
                   #c % 3 == 0 na expressão ele quer os numeros que são divididos por 3 e que tem resto 0

            cont = cont + 1 # #Toda vez que for encontrado um número que atende as condições ele vai contar
            soma = soma + c #A soma entre todos os valores que foram pedidos no for
print('A soma de todos os {} valores é de {}'.format(cont, soma))