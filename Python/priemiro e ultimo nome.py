nome = str(input('Favor escrever seu nome :')).strip()
div = nome.split()
print('Seu primeiro nome é: {}'.format(div[0]))
print('Seu ultimo nome é: {}'.format(div[len(div)-1]))
