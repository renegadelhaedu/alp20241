'''
#arq = open('alunos.txt', 'w')#escrita, ele cria e sobrescreve
arq = open('alunos.txt', 'a')#atualiza, ele cria e nao sobrescreve
#arq = open('alunos.txt', 'r')#leitura

lim = 4
for qtde in range(lim):
    nome = input('digite seu nome')
    nota = float(input('digite sua nota'))
    if(qtde != lim - 1):
        arq.write(nome + ',' + str(nota) + '\n')
    else:
        arq.write(nome + ',' + str(nota))

arq.close()

'''

arq = open('alunos.txt', 'r')#leitura

linhas = arq.readlines()
soma = 0
qtde_validas = 0
print(f'a quantidade de linhas deste arquivo e: {len(linhas)}')
for linha in linhas:
    if(len(linha) > 1):
        soma += float(linha)
        qtde_validas += 1
media = round(soma / qtde_validas, 2)
print(f'a media de notas foi {media}')


arq.close()

