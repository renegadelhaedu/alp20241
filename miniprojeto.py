from usuarios import *
import usuarios as usr
import menus

usuarios = {}
filmes = []
opmenu_pr = 99

def validar_capacidade(texto):
    campo = int(input(texto))
    while (campo < 0):
        campo = int(input(texto))
    return campo

def validar_valor(texto):
    campo = float(input(texto))
    while (campo < 0):
        campo = float(input(texto))
    return campo

def validar_campo(texto):

    campo = input(texto)
    while(len(campo) == 0):
        campo = input(texto)
    return campo

def gerar_filme():
    nome = validar_campo('digite o nome')
    gen = validar_campo('digite o genero')
    sinopse = validar_campo('digite a sinopse do filme')
    capacidade = validar_capacidade('qual a capacidade')
    valor = validar_valor('digite o valor do ingresso')

    return {'nome':nome,'genero':gen, 'sinopse':sinopse,
                               'capacidade':capacidade, 'valor':valor}

def exibir_lista_com_busca(filmes):
    busca = input('digite o nome do filme')
    for i in range(len(filmes)):
        if (busca in filmes[i]['nome']):
            print(f'{i} - {filmes[i]["nome"]}')


while(opmenu_pr != 0):

    menus.menu_principal()
    opmenu_pr = int(input('\ndigite a opcao desejada'))

    if(opmenu_pr == 1):
        login = input('digite seu login')
        senha = input('digite sua senha')

        logado = fazer_login(login, senha, usuarios, 2)

        if(logado):
            print('Login realizado com sucesso')
            menus.menu_adm()

            opadm = int(input('digite a opcao desejada'))
            if(opadm == 1):

                filmes.append(gerar_filme())
                print('filme adicionado com sucesso')

            elif(opadm == 2):
                exibir_lista_com_busca(filmes)
            elif (opadm == 3):
                exibir_lista_com_busca(filmes)
                cod_filme = int(input('digite o codigo do filme para atualizar'))

                filmes[cod_filme] = gerar_filme()
                print('filme atualizado com sucesso')

            elif(opadm == 4):
                exibir_lista_com_busca(filmes)
                cod_filme = int(input('digite o codigo do filme para atualizar'))
                filmes.pop(cod_filme)
                print('filme removido com sucesso')

        else:
            print('Senha ou usuario inválido')

    elif(opmenu_pr == 2):
        login = input('digite seu login')
        senha = input('digite sua senha')

        logado = fazer_login(login, senha, usuarios, 1)


        if(logado):
            print('Login realizado com sucesso')
            menus.menu_cliente()
        else:
            print('Senha ou usuario inválido')

    elif (opmenu_pr == 3):
        usr.cadastrar_user(usuarios)