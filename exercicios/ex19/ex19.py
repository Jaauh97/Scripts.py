import random
print('='*60)
print('Um professor vai sortear um de seus quatro alunos para apagar o quadro')
print('Entre os alunos estão: Joao , Erivaldo , Kaua e Francisco')
space = input('Aperte enter em seu tecaldo e saiba quem foi escolhido: '
              '')
num1 = random.randint(1, 4)
print('O aluno escolhido foi o número {} , Joao.'.format(num1))
print('='*60)

