arquivo = open('casa.txt','r')
linhas = arquivo.readlines()
qtde_aprov = 0
for linha in linhas:
    if(linha.count('media') > 0):
        print(linha)
    elif(float(linha) >= 7):
        qtde_aprov += 1

arquivo.close()

print(f'nesta turma foram {qtde_aprov} aprovados')
