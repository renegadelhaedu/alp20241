#fizemos uma modificacao para so aceitar idades multiplas de 10
n = int(input("digite o numero de alunos: "))
soma = 0
count = 0
for x in range(n):
    idade = int(input("Digite a idade: "))
    if(idade % 10 != 0):
        soma = idade + soma
        count = count + 1

media = soma / count

if media <= 25:
    print("A media da sala é jovem")
elif media <= 60:
    print("A media da sala é adulta")
else:
    print("A media da sala é idosa")
print(media)