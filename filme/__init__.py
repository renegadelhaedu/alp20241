import validacoes as valid

def gerar_filme():
    nome = valid.validar_campo('digite o nome')
    gen = valid.validar_campo('digite o genero')
    sinopse = valid.validar_campo('digite a sinopse do filme')
    capacidade = valid.validar_capacidade('qual a capacidade')
    valor = valid.validar_valor('digite o valor do ingresso')

    return {'nome':nome,'genero':gen, 'sinopse':sinopse,
                               'capacidade':capacidade, 'valor':valor}


def exibir_lista_com_busca(filmes):
    busca = input('digite o nome do filme')
    for i in range(len(filmes)):
        if (busca in filmes[i]['nome']):
            print(f'{i} - {filmes[i]["nome"]}')
