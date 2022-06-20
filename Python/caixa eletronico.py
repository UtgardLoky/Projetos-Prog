saq = int(input('Qual o valor a ser sacado: '))

#while saq % 50 and 20 and 10 and 1 != 0:
c = saq // 50
v = (saq % 50) // 20
d = (saq % 50 // 20) // 10
u = saq % 10

print(f'''Total de notas de 50: {c}
Total de notas de 20: {v}
Total de notas de 10: {d}
Total de notas de 1: {u}''')

