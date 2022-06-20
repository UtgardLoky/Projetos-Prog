num_list = []
a = []
b = []

for x in range(1,6):
    num_list.append(int(input(f'Favor digitar o {x}\u00ba numero: ')))

for i, v in enumerate(num_list):
    if v == max(num_list):
        a.append(i)
    if v == min(num_list):
        b.append(i)

print(f'Vc digitou os valores {num_list}')
print(f'''O maior valor foi {max(num_list)}, ele está na posição {a}
O menor valor foi {min(num_list)}, ele está na posição {b}''')

