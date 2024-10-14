sal = int(input('Digite seu salário, para que possamos calcular seu aumento: '))
if sal >= 1.250:
 sal1 = (sal*10)/100   
 print('Seu salário é {} e seu aumento foi de {}'.format(sal,sal1))
 print(sal1)
else:
    sal2 = (sal*15)/100
    print('Seu salário é {} e seu aumento foi de {}'.format(sal,sal2))
    print(sal2)
    
    \\correção
    
sala = float(input('Digite seu salário R$: ')) 
if sala <= 1250: 
    novo = sala + (sala*15 / 100)
else:
    