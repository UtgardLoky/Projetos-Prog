#declara variaveis
num_lista = []

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
