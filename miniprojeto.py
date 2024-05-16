usuarios = {}
filmes = []
opmenu_pr = 99

while(opmenu_pr != 0):

    print('------------------Menu-------------------\n')
    print('1-Gerenciar Filmes')
    print('2-Comprar ingresso')
    print('3-Cadastrar usuário')
    print('0-Sair do sistema')

    opmenu_pr = int(input('\ndigite a opcao desejada'))

    if(opmenu_pr == 1):
        login = input('digite seu login')
        senha = input('digite sua senha')

        logado = False
        for chave in usuarios:
            if(chave == login and usuarios[login][2] == senha and usuarios[login][1] == 2):
                logado = True

        if(logado):
            print('Login realizado com sucesso')
            print('\n---- Menu do administrador---')
            print('1-cadastrar filme')
            print('2-buscar filme')
            print('3-atualizar filme')
            print('0-Logout')

            opadm = int(input('digite a opcao desejada'))
            if(opadm == 1):
                nome = input('digite o nome')
                gen = input('digite o genero')
                sinopse = input('digite a sinopse')
                capacidade = int(input('qual a capacidade'))
                valor = float(input('digite o valor do ingresso'))

                filmes.append({'nome':nome,'genero':gen, 'sinopse':sinopse,
                               'capacidade':capacidade, 'valor':valor})
                print('filme adicionado com sucesso')

            elif(opadm == 2):
                busca = input('digite o nome do filme')
                for filme in filmes:
                    if(busca in filme['nome']):
                        print(filme)

            elif (opadm == 3):
                busca = input('digite o nome do filme')
                for i in range(len(filmes)):
                    if(busca in filmes[i]['nome']):
                        print(f'{i} - {filmes[i]["nome"]}')
                cod_filme = int(input('digite o codigo do filme para atualizar'))

                nome = input('digite o nome')
                gen = input('digite o genero')
                sinopse = input('digite a sinopse')
                capacidade = int(input('qual a capacidade'))
                valor = float(input('digite o valor do ingresso'))

                filmes[cod_filme] = {'nome': nome, 'genero': gen, 'sinopse': sinopse,
                               'capacidade': capacidade, 'valor': valor}
                print('filme atualizado com sucesso')

            elif(opadm == 3):
                busca = input('digite o nome do filme')
                for i in range(len(filmes)):
                    if (busca in filmes[i]['nome']):
                        print(f'{i} - {filmes[i]["nome"]}')
                cod_filme = int(input('digite o codigo do filme para atualizar'))
                filmes.pop(cod_filme)
                print('filme removido com sucesso')

        else:
            print('Senha ou usuario inválido')

    elif(opmenu_pr == 2):
        login = input('digite seu login')
        senha = input('digite sua senha')

        logado = False
        for chave in usuarios:
            if(chave == login and usuarios[login][2] == senha ):
                logado = True


        if(logado):
            print('Login realizado com sucesso')
            print('---- Menu do Cliente---')
        else:
            print('Senha ou usuario inválido')

    elif (opmenu_pr == 3):
        print('\n---Cadastro de usuário---\n')
        nome = input('digite seu nome completo')
        login = input('digite seu login')
        senha = input('digite sua senha')
        perfil = int(input('digite 1 para cliente do cinema ou 2 para administrador do cinema'))

        usuarios[login] = [nome, perfil, senha]
        print('Cadastro realizado com sucesso!!!\n')