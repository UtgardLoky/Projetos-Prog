a = int(input('Favor entrar com um numero para saber se este é primo: '))

for c in range (1, a):
    if a % c != 0 or a // a == 1:
        print('O numero {} é primo!' .format(a))

    else:
        print('O numero {} não é primo!'.format(a))


