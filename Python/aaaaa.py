
def inverter(numero):
    inverso = 0
    while (numero != 0):
        # temp recebe o resto da divisão do número por 10
        temp = numero % 10
        # e vamos guardando no inverso
        inverso = inverso * 10 + temp
        # número recebe ele dividido por 10
        numero = numero // 10
    return inverso

#Variaveis
x = 1
resultado = []

for numero in range(1000):
    inverso = inverter(numero)
    soma = numero + inverso
    if soma % 2 != 0 and soma < 1000000 and numero % 10 != 0:
        print(f'{x}º {numero} + {inverso} = {soma}')
        resultado.append(numero)
        x += 1
    if soma >= 1000:
        break
print(resultado)
print(f'Existem {len(resultado)} numeros com n + reverso(n) resultando'
                f' em números ímpares que estão abaixo de 1 milhão.')