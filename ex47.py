arq_nomes = open('nomes.txt','a')
arq_notas = open('notas.txt','a')

while(True):
    nome = input('digite seu nome ou a palavra sair para encerra o codigo')

    if(nome.upper() == 'SAIR'):
        break
    nota = float(input('digite sua nota'))
    arq_nomes.write('\n' + nome)
    arq_notas.write('\n' + str(nota))

arq_notas.close()
arq_nomes.close()