num1 = float(input("Por favor digite um numero: "))
num2 = float(input("Por favor digite mais um numero: "))
num3 = float(input("Por favor digite mais um numero: "))
primeiro = float
segundo = float
terceiro = float

if num1 > num2:
   if num1 > num3:
     primeiro = num1
     if num2 > num3:
       segundo = num2
       terceiro = num3
     else:
       segundo = num3
       terceiro = num2
   else:
     primeiro = num3
     segundo = num1
     terceiro = num2
else:
  if num2 > num3:
     primeiro = num2
     if num1 > num3:
       segundo = num1
       terceiro = num3
     else:
       segundo = num3
       terceiro = num1
  else:
     primeiro = num3
     segundo = num2
     terceiro = num1


print(primeiro + segundo)