
def fazer_login(login, senha, dicionario, tipo):
    for chave in dicionario:
        if (chave == login and dicionario[login][2] == senha and dicionario[login][1] == tipo):
            return True
    return False


def cadastrar_user(dicionario):
    print('\n---Cadastro de usuário---\n')
    nome = input('digite seu nome completo')
    login = input('digite seu login')
    senha = input('digite sua senha')
    perfil = int(input('digite 1 para cliente do cinema ou 2 para administrador do cinema'))

    dicionario[login] = [nome, perfil, senha]
    print('Cadastro realizado com sucesso!!!\n')