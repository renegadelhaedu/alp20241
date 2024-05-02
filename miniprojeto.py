usuarios = {}
sessao = list()
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
            if(chave == login and usuarios[login][2] == senha ):
                logado = True

        if(logado):
            print('Login realizado com sucesso')
            print('---- Menu do administrador---')
            print('1-cadastrar filme')
            print('2-... filme')
            print('3-... filme')
            print('0-Logout')
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

        usuarios[login] = [login, nome, perfil, senha]
        print('Cadastro realizado com sucesso!!!\n')