dist = float(input('Favor digitar a distancia de sua viagem: '))
if dist <= 200:
    print('Sua viagem custará R${:.2f}.' .format(dist*0.5))
else:
    print('Sua viagem custará R${:.2f}.' .format(dist*0.45))
