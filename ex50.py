#faça um algoritmo em python para ler o nome de 15 pessoas
#e verificar quantas delas tem nomes maiores que 10 letras
nomes = list()

for i in range(15):
    nomes.append(input('digite seu nome'))

qtde = 0
for nome in nomes:
    if(len(nome) > 10):
        qtde += 1


print(qtde)