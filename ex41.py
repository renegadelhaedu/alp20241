arquivo = open('casa.txt','a')
media_turma = 0
qtde = 0
while(True):
    nome = input('digite seu nome ou a palavra sair')
    if(nome == 'sair'):
        break
    nota = float(input('digite sua nota'))
    media_turma += nota
    qtde += 1
    arquivo.write(nome + ':' + str(nota) + '\n')

if(qtde > 0):
    media_turma = media_turma / qtde
    arquivo.write('media: ' + str(media_turma) + '\n')
arquivo.close()
#modifique este code para ler o nome do aluno e salvar
#o nome e a nota dele no arquivo txt. manter calculo media
