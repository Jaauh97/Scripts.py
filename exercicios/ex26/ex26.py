#name = str(input('Digite um nome: ')).upper().strip()
#print('A letra A aparece {} vezes na frase. '.format(name.count('A')))
#print('A primeira letra A apareceu na posição {}'.format(name.find('A')))
#print('A ultima ocorrencia de A foi em {}'.format(name.rfind('A')))

# o find procura a numeracao da palavara na qual e colocada para procurar


frase = str(input('Digite uma frase qualquer: ')).upper().strip()
letra = str(input('Digite a letra que quer análisar: ')).upper().strip()
print('A letra {} apareceu {} vezes'.format(letra,frase.count('a')+1))