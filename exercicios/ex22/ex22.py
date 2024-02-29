nome = str(input('Digite um nome completo:'))
div = nome.split()
print('Se nome todo em letras maiúsculas é assim: ',nome.upper())
print('Seu nome todo em letras minúsculas é assim: ',nome.lower())
print(len(nome))
print('Seu primeiro nome tem ',len(div[0]),' Letras')


#correção

name = str(input('Digite seu nome completo: ')).strip()

print('Seu nome todo com letras maiúsculas fica assim: {}'.format(name.upper()))
print('Seu nome todo com letras minúsculas fica assim {}'.format(name.lower()))
print('Seu nome todo possui um total de {} letras'.format(len(name) - name.count(' ')))
print('Seu primeiro nome tem {}  letras'.format(name.find(' ')))

# em name.count ele vai contar quantos espacos (ou algo que voce digite dentro do parenteses) e adiciona a funcao menos

# em name.find ele vai contar quantas letras existem antes do primeiro
# espaco ou antes da primeira coisa que colocar entre parenteses

