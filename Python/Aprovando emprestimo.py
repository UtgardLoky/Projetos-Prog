casa = float(input('Favor informar o valor da casa desejada: '))
salario = float(input('Favor informar seu salario: '))
tempo = float(input('Em quantos anos gostaria de pagar a casa? '))
prestacao = casa // (tempo * 12)

if (0.3 * salario) >= prestacao:
   situacao = 'aprovado'
else: situacao = 'reprovado'

print('Seu emprestimo foi {}' .format(situacao))

