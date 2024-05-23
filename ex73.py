'''
arquivo -> criar, inserir,leitura

buscar,atualizar,remover conteúdo

w = escrita (sobrescreve)
a = atualizar
r = leitura
'''

notas = open('sj.txt', 'a')

for i in range(2019,2024):

    nota = int(input('digite a qtde de pessoas que vc dancou em ' + str(i)))

    notas.write(f'{i},{nota}\n')

notas.close()
#guilherme
#qtde de pessoas que ele dancou
