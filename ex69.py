#funcoes
alunos = [{'nome':'rene', 'media': 5.2},{'nome':'maria', 'media': 9.3},{'nome':'jose', 'media': 8.1}]
monitores = [{'nome':'toinho', 'media': 7.2},{'nome':'zezinha', 'media': 9.9},{'nome':'felipe', 'media': 1.1}]

def nome_maior_nota(lista):
    nome_maior = ''
    nota_maior = 0
    for aluno in lista:
        if(aluno['media'] > nota_maior):
            nome_maior = aluno['nome']
            nota_maior = aluno['media']
    return nome_maior

print(nome_maior_nota(alunos))