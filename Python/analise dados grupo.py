sf = 0
sm = 0
c = 0
s = 0
while True:
    idad = int(input('Favor digite sua idade: '))
    sex = str(input('Favor digite seu sexo: ')).strip().lower()

    if idad >= 18:
        c += 1
    if sex[0] == 'f':
        if idad < 20:
            s += 1
    else:
        sm += 1

    t = input('Deseja continuar: ').lower().strip()
    if t[0] == 'n':
        break

print(f'''      {c} pessoas tem mais de 18 anos'
      {sm} homens foram cadastrados'
      {s} mulheres tem menos de 20 anos''')
