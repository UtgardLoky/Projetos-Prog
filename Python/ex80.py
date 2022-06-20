#Variaveis
num_lista = []

#Recebe dados
for x in range(5):
    n =(float(input('Favor digitar um numero: ')))

#inicia sistema e verifica se maior que ultimo numero da lista
    if x == 0 or n > num_lista[-1]:
        num_lista.append(n)

#analisa em que posição inserir o numero(ordem crescente)
    else:
        pos = 0
        while pos < len(num_lista):
            if n <= num_lista[pos]:
                num_lista.insert(pos, n)
                break
            pos += 1

#Exibi lista ordem crescente
print(num_lista)
