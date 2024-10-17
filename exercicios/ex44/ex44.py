print('{:=^40}'.format(' Loja do Jaauh ')) #:=^40 é um estilo de formatação de que deixa o texto no centro

preco = float(input('Qual o valor das compras: '))

print('''Formas de pagamento:
[ 1 ] á vista 
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')

opcao = int(input('Qual a opção de pagamento: '))

if opcao == 1:
    total = preco - (preco *10 / 100)
elif opcao == 2:
    total = preco - (preco *5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas: '))
    parcela =  total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(totalparc , parcela))
print('Sua comprar de R${:.2f} vai custar R${:.2f} no final.'.format(preco , total))