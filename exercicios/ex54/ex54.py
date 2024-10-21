from datetime import date #importei a date pra pega a data atual

atual = date.today().year #Declarei o ano atual com variavel
totmaior = 0
totmenor = 0 #Declarei valor 0 para as variáveis

for pess in range(1, 8):
    nasc = int(input('Em que ano a {} pessoa nasceu: '.format(pess)))#Coloquei esse pess para poder ir adicionando numero nas perguntas EX: 1 pessoa
    idade = atual - nasc  #Declarei a idade da pessoa, através de soma básica . O ano atual menos o ano que a pessoa nasceu
    
    if idade >= 21: #Se idade maior que 21 então vai adionar mais 1 de valor
        totmaior += 1
    else:
        totmenor += 1 #Se idade menor que 21 então vai adionar mais 1 de valor
print('Ao todo tivemos {} maiores de idade e tivemos {} menores de idade'.format(totmaior, totmenor))      
         
    

