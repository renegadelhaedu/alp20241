import usuarios as usr
import menus
import filme

usuarios = {}
filmes = []
opmenu_pr = 99

while(opmenu_pr != 0):

    menus.menu_principal()
    opmenu_pr = int(input('\ndigite a opcao desejada'))

    if(opmenu_pr == 1):
        login = input('digite seu login')
        senha = input('digite sua senha')

        #ADM
        logado = usr.fazer_login(login, senha, usuarios, 2)

        if(logado):
            print('Login realizado com sucesso')
            menus.menu_adm()

            opadm = int(input('digite a opcao desejada'))
            if(opadm == 1):

                filmes.append(filme.gerar_filme())
                print('filme adicionado com sucesso')

            elif(opadm == 2):
                filme.exibir_lista_com_busca(filmes)
            elif (opadm == 3):
                filme.exibir_lista_com_busca(filmes)
                cod_filme = int(input('digite o codigo do filme para atualizar'))

                filmes[cod_filme] = filme.gerar_filme()
                print('filme atualizado com sucesso')

            elif(opadm == 4):
                filme.exibir_lista_com_busca(filmes)
                cod_filme = int(input('digite o codigo do filme para atualizar'))
                filmes.pop(cod_filme)
                print('filme removido com sucesso')

        else:
            print('Senha ou usuario inválido')

    elif(opmenu_pr == 2):
        login = input('digite seu login')
        senha = input('digite sua senha')

        #cliente
        logado = fazer_login(login, senha, usuarios, 1)

        if(logado):
            print('Login realizado com sucesso')
            menus.menu_cliente()
        else:
            print('Senha ou usuario inválido')

    elif (opmenu_pr == 3):
        usr.cadastrar_user(usuarios)