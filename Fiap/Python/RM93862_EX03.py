#Variaveis
somaimpar = float(0)
somapar = float(0)

#coleta as notas alunos ímpares e calcula média
for x in range (1,50,2):
    notaimpar = float(input(f'''VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES
POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {x}: '''))
    somaimpar += notaimpar
    mediaimpar = somaimpar / 25
print('\n' * 3)

#coleta as notas alunos pares e calcula média
for x in range (2,51,2):
    notapar = float(input(f'''VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES
POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {x}: '''))
    somapar += notapar
    mediapar = somapar / 25
print(' ')

#Verifica qual é maior
if mediapar > mediaimpar:
    result = 'A média dos alunos Pares é maior'
elif mediapar == mediaimpar:
    result = 'As medias foram iguais'
else:
    result = 'A média dos alunos Impares é maior'

#Exibi resultados
print(f'''A média dos alunos ímpares é: {mediaimpar}
A média dos alunos pares é: {mediapar}
{result}''')
