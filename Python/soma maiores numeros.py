maior = segundo = 0

for c in range (0, 3):
    num = float(input("Digite os numeros : "))
    if c == 0:
        maior = num
    else:
        if num > maior:
            segundo = maior
            maior = num
        elif num > segundo:
            segundo = num

print("O maior numero é {} e o segundo maior numero é {}, a soma é {}." .format(maior, segundo, maior+segundo))
