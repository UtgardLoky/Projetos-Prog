#Solitando dados do usuário
faturamento = float(input('Favor digite o valor do seu faturamente anual: '))
assinatura = int(input("""
[1] Basic
[2] Silver
[3] Gold
[4] Platinum

Favor escolher sua assinatura: """))

#Calculando valor bonus a pagar
if assinatura == 1:
    pagamento = faturamento * 0.3
elif assinatura == 2:
    pagamento = faturamento * 0.2
elif assinatura == 3:
    pagamento = faturamento * 0.1
else:
    pagamento = faturamento * 0.05

#Exibe valor a pagar
print(f'\nO senhor deve o montante de R${pagamento:.2f} referente ao bonus.')
