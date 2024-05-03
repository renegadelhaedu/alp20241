pessoas = {'felipe':'maria', 'popo':'penelope', 'jose':'nyvi'}

busca = input('digite o nome do cidadao')

for pessoa in pessoas:
    if(busca in pessoa):
        novoamor = input('digite o nome do novo amor desta pessoa')
        pessoas[pessoa] = novoamor

print(pessoas)
