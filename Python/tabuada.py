while True:
    tab = int(input('Escolha a tabuada desejada ou digite 0 para encerrar: '))

    if tab == 0:
        break

    for c in range (0, 11):
        print('{} x {} = {}' .format(c, tab, c * tab))

