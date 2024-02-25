# peradores aritiméticos 

# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# ** Potência
# // Divisão Inteira
# %  Resto Da Devisão
# == Igual

# Ordem De Precedencência 

# 1 ()
#2 **
#3 * , / , // , %
#4 + -

#teste

#s = 5+3*2 #11
#print(s)
#s1 = 3*5+4**2 #31
#print(s1)
#s2 = 3*(5+4)**2 #243 
#print(s2)

#n1 = int(input('Digite um valor: '))
#n2 = int(input('Digite outro valor: '))
#print('A soma dos 2 valores é igual a {}'.format(n1+n2))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n2 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2

print ('>>>A soma é {}, o produto é {}, e divisão {:2f}'.format(s,m,d) , end=' ')
print ('A divisão inteira {}, e a potência {}'.format(di,p))

# :3f serve para controlar o numero de descimais que aparecem apos o ponto ex: 1.3333333 ou 1.333
# end=' '  Serve para nao quebrar linhas , quando há 2 prints juntos 
# \n Serve para quebrar linhas em print 