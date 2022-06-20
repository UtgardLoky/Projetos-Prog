num1 = float(input("Por favor digite um numero: "))
num2 = float(input("Por favor digite mais um numero: "))
num3 = float(input("Por favor digite mais um numero: "))
maior = num1
menor = num1


#Verificando o maior numero
if num2 > num1 and num2 > num3:
   maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

#Verificando o menor numero
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

print('O maior numero digitado foi {}' .format(maior))
print('O menor numero digitado foi {}' .format(menor))
