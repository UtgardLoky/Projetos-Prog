n = int(input("Digite: "))
ultimo=1
penultimo=1
a = ""
if n == 1 or n == 0:
    print('Este numero pertence a sequencia')

else:
    for count in range(0,n):
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        if termo == n:
            a = 'Este numero pertence a sequencia'
        else:
            b = 'este termo não pertence a sequencia'

    if a == 'Este numero pertence a sequencia':
        print(a)
    else:
        print(b)
