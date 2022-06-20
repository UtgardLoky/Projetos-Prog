from funcao import isnumber

#listas
num_lista = []
par_lista = []
impar_lista = []

#Coleta dados
while True:
    x = (input('\nDigite fim para fechar o sistema.\nFavor digitar um numero: '))

    if x.lower().strip() == 'fim':
        break
    elif isnumber(x):
        x = float(x)
        num_lista.append(x)
        # Verifica se é par ou impar
        if x % 2 == 0:
            par_lista.append(x)
        else:
            impar_lista.append(x)
    else:
        print('\nPor favor digite somente numeros.')

#Exibi listas
print(f'Lista Completa: {num_lista}\nLista de numeros pares: {par_lista}\nLista de numeros impares: {impar_lista}')
