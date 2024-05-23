'''
arquivo -> criar, inserir,leitura

buscar,atualizar,remover conteúdo

w = escrita (sobrescreve)
a = atualizar
r = leitura
'''

import matplotlib.pyplot as plt

anos = list()
qtde = list()
notas = open('sj.txt', 'r')

linhas = notas.readlines()

for linha in linhas:
    anos.append(int(linha.split(',')[0]))
    qtde.append(int(linha.split(',')[1].replace('\n','')))

notas.close()

tipo = input('digite barra se quiser um grafico de barra ou linha caso contrario')
if(tipo.lower() == 'barra'):
    plt.bar(anos, qtde)
else:
    plt.plot(anos, qtde)
plt.show()



#guilherme
#qtde de pessoas que ele dancou
