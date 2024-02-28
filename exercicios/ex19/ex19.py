import random
print('='*60)
print('Um professor vai sortear um de seus quatro alunos para apagar o quadro')
print('Entre os alunos estão: Joao , Erivaldo , Kaua e Francisco')
space = input('Aperte enter em seu tecaldo e saiba quem foi escolhido: '
              '')
num1 = random.randint(1, 4)
print('O aluno escolhido foi o número {} , Joao.'.format(num1))
print('='*60)



#Para escolhas random , crie uma lista = [] coloque as variaveis dentro e solicite o cmd choice
n1 = str(input('Nome do primeiro aluno: '))
n2 = str(input('Nome do Segundo aluno: '))
n3 = str(input('Nome do terceiro aluno: '))
n4 = str(input('Nome do quarto aluno: '))

lista = [n1, n2, n3, n4]
print('O aluno escolhido foi {}'.format(random.choice(lista)))