def casar(pessoa1:str, pessoa2:str) -> str:
    if(pessoa1 == 'rene' or pessoa2 == 'rene'):
        return 'vai dar tudo errado'
    else:
        return f'{pessoa1} vai ser muito feliz com {pessoa2}'


def filtrar_pessoas(lista:list):
    selecao = []
    for pessoa in lista:
        if(pessoa != 'fernandinho' and pessoa != 'marcola'):
            selecao.append(pessoa)
    return selecao

def analisar_dados(conjunto:set):
    maior = -99999999
    menor =  99999999
    for num in conjunto:
        if(num > maior):
            maior = num
        if(num < menor):
            menor = num
    return maior, menor, None


def preencher(lista:list):
    item = input('me informe o nome do elemento para adicionar na lista ')
    lista.append(item)
    cont = input('digite se deseja informar outro nome do elemento ')
    if(cont.lower() == 'sim'):
        preencher(lista)
    return lista

vazia = list()
cheia = preencher(vazia)
print(cheia)

for i in range(100000):
    vazia.append(input('digite o nome do lelemtn ....'))
    cont = input('digite se deseja informar outro nome do elemento ')
    if(cont.lower() != 'sim'):
        break
