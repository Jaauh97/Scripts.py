peso = float(input('Qual seu peso? '))
alt = float(input('Qual sua altura? '))
imc = peso / (alt * alt)

if imc < 18.5:
    print('Seu IMC é de \033[1:31m{:.2f}'.format(imc))
    print('Você está \033[1:31mabaixo do peso')

elif imc == 18.5 or imc <= 25:
    print('Seu IMC é de \033[1:32m{:.2f}'.format(imc))
    print('Você está no seu \033[1:32mpeso ideal ')

elif imc == 26 or imc <= 30:
    print('Seu IMC é de \033[1:33m{:.2f}'.format(imc))
    print('Você está com \033[1:33msobrepeso ')

elif imc == 31 or imc <= 40:
    print('Seu IMC é de \033[1:35m{:.2f}'.format(imc))
    print('Você está \033[1:35mobeso')

else:
    print('Seu IMC é de \033[1:31m{:.2f}'.format(imc))
    print('Você está com \033[1:31mobesidade mórbida')


