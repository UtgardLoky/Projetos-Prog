c = 0
soma = 0

while True:
    n = int(input("favor digitar um numero (digite 999 para encerrar) :"))
    if n == 999:
        break
    c+= 1
    soma += n

print(f'O total de numeros digitados foi {c}, a soma dos numeros é {soma}')
