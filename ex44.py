arq = open('JH.txt', 'r')
linhas = arq.readlines()
qtde_contatinhos = 0
for linha in linhas:
    if(int(linha) >= 18 and int(linha) <= 50):
        qtde_contatinhos += 1

arq.close()
print(f'em olinda, vou manter contato com {qtde_contatinhos}')