pessoas = list()


while(True):
    nome = input('digite seu nome ou digite sair')
    if(nome == 'sair'):
        break
    idade = 23

    pessoas.append([nome, idade])

busca = input('digite o nome do usuario que vc deseja atualizar')
for i in range(len(pessoas)):
    if(pessoas[i][0] == busca):
        novoNome = input(f'digite o nome do usuario que esta no indice {i}')
        pessoas[i][0] = novoNome

for pessoa in pessoas:
    print(f'nome: {pessoa[0]} - idade:{pessoa[1]} ')
