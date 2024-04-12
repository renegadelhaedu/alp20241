arquivo = open('casa.txt','a')
media_turma = 0
for i in range(3):
    nome = input('digite seu nome')
    nota = float(input('digite sua nota'))
    media_turma += nota

    arquivo.write(nome + ':' + str(nota) + '\n')
media_turma = media_turma / 3

arquivo.write('media: ' + str(media_turma) + '\n')
arquivo.close()
#modifique este code para ler o nome do aluno e salvar
#o nome e a nota dele no arquivo txt. manter calculo media
