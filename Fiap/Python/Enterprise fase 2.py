ind = ['EMPRESA', 'SENHA', 'AJUDA DE SENHA', 'NÚMERO DO TELEFONE', 'NOMES', 'E-MAIL', 'DATA DE VAZAMENTO']
test = []

info = [
['DriveSure', 'sim', 'não', 'sim', 'sim', 'sim', '2020/12/01'],
['bigbasket', 'sim', 'não', 'sim', 'sim', 'sim', '2020/10/01'],
['Appen', 'sim', 'não', 'sim', 'sim',  'sim', '2020/06/01'],
['Vakinha', 'sim', 'não', 'sim', 'sim', 'sim', '2020/06/01'],
['Hurb', 'sim', 'não', 'sim', 'sim', 'sim', '2019/03/01'],
['Dubsmash', 'sim', 'não', 'sim', 'sim', 'sim', '2018/12/01'],
['Descomplica', 'sim', 'não', 'não', 'sim', 'sim', '2021/03/01'],
['Animal Jam', 'sim', 'não', 'não', 'sim', 'sim', '2020/10/01'],
['Aptoide', 'sim', 'não', 'não', 'sim', 'sim', '2020/04/01'],
['Canva', 'sim', 'não', 'não', 'sim', 'sim', '2019/05/01'],
['Animoto', 'sim', 'não', 'não', 'sim', 'sim', '2018/07/01'],
['Bookmate', 'sim', 'não', 'não', 'sim', 'sim', '2018/06/01'],
['Chegg', 'sim', 'não', 'não', 'sim', 'sim', '2018/04/01'],
['Army Force Online', 'sim', 'não', 'não', 'sim', 'sim', '2016/05/01'],
['Daily Quiz', 'sim', 'não', 'não','não', 'sim', '2021/01/01'],
['James', 'sim', 'não', 'não','não', 'sim', '2020/06/01'],
['AnimeGame', 'sim', 'não', 'não','não', 'sim', '2020/02/01'],
['Avvo', 'sim', 'não', 'não','não', 'sim', '2019/12/01'],
['BlankMediaGames', 'sim', 'não', 'não','não', 'sim', '2018/12/01'],
['Fotolog', 'sim', 'não', 'não','não', 'sim', '2018/12/01'],
['SHEIN', 'sim', 'não', 'não','não', 'sim', '2018/06/01'],
['Dailymotion', 'sim', 'não', 'não','não', 'sim', '2016/10/01'],
['Funimation', 'sim', 'não', 'não','não', 'sim', '2016/07/01'],
['Bitly', 'sim', 'não', 'não','não', 'sim', '2014/05/01'],
['Adobe', 'sim', 'sim', 'não','não', 'sim', '2013/10/01'],
['tumblr', 'sim', 'não', 'não', 'não', 'sim', '2013/01/01'],
['Dropbox', 'sim', 'não', 'não','não', 'sim', '2012/06/01'],
['MySpace', 'sim', 'não', 'não','não', 'sim', '2008/01/01'],
['LinkedIn', 'não', 'não', 'não', 'sim', 'sim', '2021/06/01'],
['Audi', 'não', 'não', 'sim', 'sim', 'sim', '2019/08/01'],
['Atlas Quantum', 'não', 'não', 'sim', 'sim', 'sim', '2018/08/01'],
['Apollo', 'não', 'não', 'sim', 'sim', 'sim', '2018/07/01']
]

dados = sorted(info, key=lambda info: info[6], reverse=True)

for l in range(1):
    for c in range(len(dados)):
        if dados[c][1] == 'sim':
            test.append(dados[c])

for l in range(1):
    for c in range(len(dados)):
        if dados[c][2] == 'sim' and dados[c] not in test:
            test.append(dados[c])

for l in range(1):
    for c in range(len(dados)):
        if dados[c][3] == 'sim' and dados[c] not in test:
            test.append(dados[c])

for l in range(1):
    for c in range(len(dados)):
        if dados[c][4] == 'sim' and dados[c] not in test:
            test.append(dados[c])

for l in range(1):
    for c in range(len(dados)):
        if dados[c][5] == 'sim' and dados[c] not in test:
            test.append(dados[c])

print(f'{ind}')
for c in range(len(test)):
    print(f'{c + 1:^4} {test[c]}, \n')
