#desenvolva um algoritmo para ler o nome do usuario, o salario e a idade
#este procedimento deve ser repetido para os 35 colaboradores da empresa.
#o algoritmo deve informar qual o funcionario mais jovem com maior salario.
idade_novo = 999
nome_novo = ''
salario_mais_novo = 0

for i in range(35):
    nome = input('digite seu nome')
    sal = float(input('digite seu salario'))
    idade = int(input('digite sua idade'))

    if(idade < idade_novo):
        nome_novo = nome
        idade_novo = idade
        salario_mais_novo = sal
    elif(idade == idade_novo and sal > salario_mais_novo):
        nome_novo = nome
        idade_novo = idade
        salario_mais_novo = sal

print(f'{nome_novo} e o funcionario mais novo com {idade_novo} anos')
print(f'ele possui salario de {salario_mais_novo}')
