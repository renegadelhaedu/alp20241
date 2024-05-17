#funcoes

def saudar_pessoa():
    nome = input('digite seu nome')
    msg = f'fala {nome}, seja bem-vindo'
    return nome

def calc_expoente(base, exp):
    resp = 1
    for i in range(exp):
        resp = resp * base
    return resp

base = int(input('digite a base'))
expoente = int(input('digite o expoente'))
alpha = 34
saida = alpha * calc_expoente(base, expoente)


