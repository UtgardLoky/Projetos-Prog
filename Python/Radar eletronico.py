velo = int(input('Qual a velocidade do carro?: '))
if velo <= 80:
    print('Parabens, vc esta em uma velocidade permitida')
else:
    print('Vc está em uma velocidade superior a permitida e foi multado em R${}.' .format((velo-80)*7))
