produtos = []

for i in range(4):
    nome = input('digite o nome do produto')
    preco = float(input('digite o preco do produto'))
    validade = input('digite a data de validade')
    produtos.append({'nome':nome, 'valor':preco, 'val':validade})

print('\nMENU de produtos\n')
for prod in produtos:
    print(prod['nome'])

prod_atual = input('digite o nome do produto que vc deseja atualizar o preco')
for i in range(len(produtos)):
    if(produtos[i]['nome'] == prod_atual):
        novoP = float(input('digite o novo preco do produto'))
        produtos[i]['valor'] = novoP

for p in produtos:
    print(p)
