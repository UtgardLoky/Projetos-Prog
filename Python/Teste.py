'''
validador = 0
repeat = 0
while (validador != 1):
    if repeat == 0:
        n = int(input("Digite um valor numérico inteiro: "))
    else:
        n = int(input("A ação falhou, tente novamente: "))
    n1 = 0
    n2 = 1

    cont = 0
    while cont <= n:
        n3 = n1 + n2
        n1 = n2
        n2 = n3

        if n == n3:

            validador = 1
            repeat = 0

        else:
            repeat = 1

        cont = cont + 1

print("Ação bem-sucedida!")

"""
min = int(input(': '))
contador = 1
soma = 1
while contador <= min:
    soma = soma * contador
    contador = contador + 1

print(soma)
"""


for contador in range(1,11,2):
    nota = float(input('nota: '))
    print(contador)

a = float('nan')
print('is -> {}'.format(a is a))
print('== -> {}'.format(a == a))
print((a), type(a))

#declara variaveis
num_lista = []
b = float('fim')
#coleta dados
while True:
    x = input('DIGITE FIM PARA TERMINAR: \nFavor digitar um numero: ')
    print()

#verifica encerramento sistema
    if x.lower().strip() == 'fim':
        break

#testa se é um numero e converte
    try:
        float(x)
        x = float(x)

#adiciona caso lista não contenha numero
        if x not in num_lista:
            num_lista.append(x)

#trata dados repitidos
        else:
            print('Voce já digitou esse numero\n')

# trata dados não numericos
    except ValueError:
        print('Isto não é um numero, por favor Digite um numero\n')

#exibi dados em ordem crescente
print(f'Os valores digitados foram {sorted(num_lista)}')


from itertools import combinations

lis = [1, 2, 3,4]

for i in (3, len(lis)):
    for comb in combinations(lis, i):
        if sum(comb) == 10:
            print(comb, '= 10')

# Um programa Python para imprimir todas as combinações
# com uma combinação com o próprio elemento
# também é incluído
from itertools import combinations_with_replacement

r = []

# Obtem todas as combinações de [1, 2, 3] e tamanho 2

comb = combinations_with_replacement([2, 3, 4], 5)
for i in list(comb):
    r.append(i)
    print(r)

comb1 = combinations_with_replacement([2, 3, 4], 4)
for i in list(comb1):
    r.append(i)
    print(r)

comb2 = combinations_with_replacement([2, 3, 4], 3)
for i in list(comb2):
    r.append(i)
    print(r)

for x in r:
    if sum(x) == 10:
        print(f'\n{x}')
'''

teste = {'a':'1', 'b':'2', 'c':'3'}

for key, values in enumerate(teste):
    print(key, values)
