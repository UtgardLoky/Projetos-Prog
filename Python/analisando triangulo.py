a = float(input('Por favor digite o primeiro segmento: '))
b = float(input('Por favor digite o segundo segmento: '))
c = float(input('Por favor digite o terceiro segmento: '))

#analisa as retas
if a > b + c or b > a + c or c > a + b:
    print('Esses segmentos não formam um triangulo')
elif a == b == c:
    print('Voce forma um triangulo equilátero')
elif a == b or a == c or c == b:
    print('Voce forma um triangulo isósceles')
else:
    print('Voce forma um triangulo escaleno')
