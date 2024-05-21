pessoas = dict()

def cadastrar_aluno(dicionario):
    nome = input('digite seu nome')
    idade = int(input('digite sua idade'))
    media = float(input('digite sua media'))
    if(nome in dicionario):
        return False
    else:
        dicionario[nome] = [idade, media]
        return True

def listar_alunos(dici, opcao):
    lista = list()
    if(opcao == 2):
        for chave in dici:
            if(dici[chave][1] >= 7 ):
                lista.append(chave)
    elif(opcao == 3):
        for chave in dici:
            if(dici[chave][0] < 18):
                lista.append(chave)
    return lista


while(True):
    print('1-cadastrar aluno')
    print('2-listar alunos com nota alta')
    print('3-listar alunos menores de idade')
    print('0-Sair')

    op = int(input('digite a opcao desejada'))

    if(op == 1):
        if (cadastrar_aluno(pessoas)):
            print('Pessoa cadastrada com sucesso')
        else:
            print('Erro! NOme já cadastrado')
    elif(op == 2):
        alunos = listar_alunos(pessoas, 2)
        for aluno in alunos:
            print(aluno)
    elif (op == 3):
        alunos = listar_alunos(pessoas, 3)
        for aluno in alunos:
            print(aluno)
    elif (op == 0):
        break
