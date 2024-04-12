arq = open('filmes.txt','w')

for i in range(5, 0, -1):
    nome_filme = input('informe o nome do filme')
    arq.write(str(i) + '-' + nome_filme + '\n')
arq.close()