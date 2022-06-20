valor = float(input('Qual o valor total das compras? '))
itens = ('[0]Pagamento à vista dinheiro',
         '[1]Pagamento à vista cartão',
         '[2]Pagamento em 2x',
         '[3]Pagamento 3x ou mais')

for c in range(0, 4):
    print(itens[c])

opcao = int(input('Escolha a forma de pagamento: ' ))

if opcao == 0:
    pagamento = 0.9 * valor

elif opcao == 1:
    pagamento = 0.95 * valor

elif opcao == 2:
    pagamento = valor

else:
    pagamento = valor * 1.2
    parcelas = int(input('Qual o numero de parcelas: '))

if opcao !=3:
    print('Sua escolha foi {}, total a ser pago R${}' .format(itens[opcao][3:], pagamento))

else:
    print('Sua escolha foi {}, total a ser pago R${}, {} parcelas R${}' .format(itens[opcao][3:], pagamento, parcelas, pagamento // parcelas))
