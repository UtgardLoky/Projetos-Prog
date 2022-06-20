salario = float(input('Por favor informe o seu selario: '))
if salario > 1250:
    print('Voce recebeu 10% de aumento, seu novo salario é R${}' .format(salario + salario * 0.1))
else:
    print('Voce recebeu 15% de aumento, seu novo salario é R${}' .format(salario + salario * 0.15))
