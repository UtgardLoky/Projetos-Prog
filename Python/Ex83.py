a = ""
lista = []
n = (input('Favor digite sua expressão: '))
for x in n:
    if n.count('(') == n.count(')'):
        a = 'Expressão Valida'
    else:
        b = 'Expressão invalida'

lista.append(n)

print(lista)
print(n.count('('), n.count(')'))
print(f'{a}'if a == 'Expressão Valida' else {b})
