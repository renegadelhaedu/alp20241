op = 99
lista = ['joao felipe', 'arthur zico', 'joao pedro', 'joao francisco']

while(op != 0):
    print('\n1-inserir pessoa')
    print('2-Listar pessoas')
    print('3-Buscar pessoas')
    print('4-remover pessoa')
    print('5-Atualizar pessoa')
    print('0-Sair')
    op = int(input('digite a opcao desejada: '))

    if(op == 1):
        nome = input('digite seu nome')
        lista.append(nome)
        print('\nPessoa inserida com sucesso\n')
    elif(op == 2):
        for nome in lista:
            print(nome)
    elif(op == 3):
        busca = input('digite o termo para buscar')
        for nome in lista:
            if(nome.count(busca) > 0):
                print(nome)
    elif(op == 4):
        busca = input('digite o nome para remocao')
        for i in range(len(lista)):
            if(lista[i].count(busca) > 0):
                print(f'{i} - {lista[i]}')
        ind_rem = int(input('digite o codigo do usuario para remover'))
        lista.pop(ind_rem)

    elif(op == 5):
        busca = input('digite o nome para atualizar')
        for i in range(len(lista)):
            if(lista[i].count(busca) > 0):
                print(f'{i} - {lista[i]}')
        ind_rem = int(input('digite o codigo do usuario para atualizar'))
        novo_nome = input('digite o novo nome para atualizar')
        lista[ind_rem] = novo_nome
















