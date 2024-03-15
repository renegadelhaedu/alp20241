#calcular a idade media de 35 alunos

soma = 0

for pessoa in range(5):
    idade = int(input('digite sua idade'))
    soma = soma + idade

media = soma / 5
print(media)

#1-modificar este codigo para ler idades de pessoas acima de 40 anos
#ao calcular a media nao contar com pessoas menores de 41 anos