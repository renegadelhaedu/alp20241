import random
matrix = []
linhas = int(input('digite a qtde de linhas'))
colunas = int(input('digite a qtde de colunas'))

for i in range(linhas):
    coluna = []
    for j in range(colunas):
        coluna.append(random.randint(1,9))
    matrix.append(coluna)



