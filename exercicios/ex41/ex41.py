from datetime import date

anv = int(input('Qual seu ano de nascimento? '))
atual = date.today().year
final = atual - anv

if final <= 9:
    print('Você tem {} anos , então é da categoria \033[1:33mMIRIM'.format(final))
elif final <= 14 :
    print('Você tem {} anos , então é da categoria \033[1:34mINFANTIL'.format(final))
elif final <= 19:
    print('Você tem {} anos , então é da categoria \033[1:35mJUNIOR'.format(final))
elif final == 20 :
    print('Você tem {} anos , então é da categoria \033[1:36mSENIOR'.format(final))
else:
    print('Você tem {} anos , então é da categoria \033[1:31mMASTER'.format(final))


