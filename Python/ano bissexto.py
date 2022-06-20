num = int(input('Favor digitar um ano para saber se é bissexto: '))
if num % 4 == 0 and num % 100 !=0 or num % 400 ==0:
    print('Ano {} é bissexto' .format(num))
else:
    print('ano {} não é bissexto' .format(num))
