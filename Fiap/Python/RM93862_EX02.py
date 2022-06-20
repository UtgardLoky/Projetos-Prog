#Recebe quantidade de votos
segunda = int(input('Favor informar o numero de votos de segunda-feira: '))
terca = int(input('Favor informar o numero de votos de terça-feira: '))
quarta = int(input('Favor informar o numero de votos de quarta-feira: '))
quinta = int(input('Favor informar o numero de votos de quinta-feira: '))
sexta = int(input('Favor informar o numero de votos de sexta-feira: '))

#Contabiliza votos
if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    escolhido = 'O dia da semana mais votado foi: Segunda-feira'
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    escolhido = 'O dia da semana mais votado foi: Terça-feira'
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    escolhido = 'O dia da semana mais votado foi: Quarta-feira'
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    escolhido = 'O dia da semana mais votado foi: Quinta-feira'
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    escolhido = 'O dia da semana mais votado foi: Sexta-feira'
else:
    escolhido = "houve um empate, favor realizar nova votação"

#Exibe o dia escolhido
print(f'\n{escolhido}')
