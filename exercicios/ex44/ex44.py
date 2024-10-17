print('{:=^40}'.format(' Loja do Jaauh ')) #:=^40 é um estilo de formatação de que deixa o texto no centro

preco = float(input('Qual o valor das compras: ')) #o usuário informa qual o valor da comprar

print('''Formas de pagamento: 
[ 1 ] á vista 
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''') #Menu de opções

opcao = int(input('Qual a opção de pagamento: ')) # O usuário informa qual a opção de pagamento

if opcao == 1:
    total = preco - (preco *10 / 100) #cálculo de porcentagem -10%

elif opcao == 2:
    total = preco - (preco *5 / 100) #cálculo de porcentagem -5%

elif opcao == 3:
    total = preco # total recebendo o preço do produto , sem nenhum tipo de alteração pois não tem desconto
    parcela = total / 2 #total do valor dividido por 2 , informa qual o valor das parcelas por 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros'.format(parcela))

elif opcao == 4:
    total = preco + (preco * 20 / 100) #total da compra recebendo mais %20 de juros
    totalparc = int(input('Quantas parcelas: ')) #perguntando ao usuário quantyas vezes ele vai parcelar
    parcela =  total / totalparc #O valor da parcela recebe o total do valor do produto , dividido pela quantidade de parcelas
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totalparc , parcela)) 

print('Sua comprar de R${:.2f} vai custar R${:.2f} no final.'.format(preco , total))
#FIM