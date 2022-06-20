#Coleta os minutos da maquina
min = int(input('Favor informar quantos minutos de hora a maquina marca neste momento: '))
x = 1
senha = 1

#Calcula senha(fatorial dos minutos)
while x <= min:
    senha *= x
    x += 1

#Exibi Senha
print(f'\nA senha é: LIBERDADE{senha}')
