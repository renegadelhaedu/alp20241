pessoas = list()
op = 'nao'
while(op == 'nao'):
    nome = input('digite seu nome')
    idade = int(input('digite sua idade'))
    altura = float(input('digite sua altura'))

    rua = input('digite sua rua')
    cidade = input('digite sua cidade')
    bairro = input('digite seu bairro')
    pessoas.append([nome, idade, altura, [rua, bairro, cidade]])

    op = input('se deseja sair digite sim')
soma = 0

for pessoa in pessoas:
    soma = soma + pessoa[1]

media = soma / len(pessoas)
print(f'\n a media de idades foi {media}')

