from time import sleep

print('Gostaria de ver uma queima de fogo?')
resp = int(input('''Digite:
[ 1 ] Digite 01 para sim:
[ 2 ] Digite 2 para não: '''))


if resp == 1:
    for c in range(10, 0, -1):
        sleep(1)
        print(c)
    print('🎆🎆🎆🎆BOOOOOMMMM🎆🎆🎆🎆')
else:
    print('FIM DO PROGRAMA ')

print('FIM DO PROGRAMA')