#importações funções
from funcao import isnumber

#variaveis
num_lista = []
x = ' '
#Coleta dados
while True:
    x = (input('\nDigite encerrar para fechar o sistema.\nFavor digitar um numero: '))

    if x.lower().strip() == 'encerrar':
        break
    elif isnumber(x):
        x = float(x)
        num_lista.append(x)
        x = ''
    else:
        print('\nPor favor digite somente numeros.')

if 5 in num_lista:
    a = 'está na lista'
else:
    a = 'não está na lista'

print(f'\nforam digitados {len(num_lista)} numeros')
print(f'Esses foram os numeros digitados:\n{list(reversed(num_lista))}')
print(f'O valor 5 {a} e foi digitado {num_lista.count(5)}')
