nomes = ['rene','mary jane','maria augusta','ana maria ']

result = []

for nome in nomes:
    if(nome.count('maria') > 0):
        result.append(nome)

print('as marias encontradas foram:')
for i in result:
    print(i)


