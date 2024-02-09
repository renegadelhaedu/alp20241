#faça um algoritmo em python para ler o nome, a idade e o ano atual.
#O programa deve calcular e exibir na tela o ano de nascimento do user

nome = input('Digite seu nome')
idade = int(input('Digite sua idade'))
anoatual = int(input('Digite o ano atual'))

anoemquenasceu = anoatual - idade

print(f'{nome} nasceu em {anoemquenasceu}')