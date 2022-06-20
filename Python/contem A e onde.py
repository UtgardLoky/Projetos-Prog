nome = str(input('Favor digitar uma frase: ')).lower().strip()
print('Sua primeira letra A está na posição {}.'.format(nome.find('a')+1))
print('Sua ultima letra A está na posição {}.' .format(nome.rfind('a')+1))
print('Sua frase tem {} letras A.' .format(nome.count('a')))
