vogais = ['a','e','i','o','u']

carac = []

for i in range(10):
    c = input('digite o caractere')
    carac.append(c)

qtde = 0
for letra in carac:
    if(letra in vogais):
        qtde += 1

#ou esta solucao
    teste = 0
    for vogal in vogais:
        if(vogal != letra):
            teste = teste + 1
    if(teste == 5):
        qtde += 1
print(qtde)