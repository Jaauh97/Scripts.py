name = str(input('Digite seu nome completo: ')).strip()
print('no nome {} possui a palavara SILVA ?'.format(name), 'silva'in name)

#correção

nome = str(input('Digite um nome: ')).strip()
print('Seu Nome tem Silva? {}'.format('silva' in nome.lower()))

#Nesse tipo de caso de procurar palavar , sempre adicione ,upper ou .lower , pq ai mesmo que o usuario escreva de qlq
#forma ele vai converter o texto e ler da maneira certa

