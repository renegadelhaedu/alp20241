#desenvolva um algoritmo para ler a idade,o nome e a altura
# dos alunos da sala. a quantidade de alunos é indeterminada.
#o programa deve calcular a maior altura e a media das idades
maiorAltura = 0
opcao = 'sim'
somaIdades = 0
qtdeAlunos = 0
while(opcao == 'sim'):
    nome = input('digite seu nome')
    idade = int(input('digite sua idade'))
    altura = float(input('digite sua altura'))

    if(altura > maiorAltura):
        maiorAltura = altura

    somaIdades = somaIdades + idade
    qtdeAlunos = qtdeAlunos + 1

    opcao = input('digite sim se voce quiser continuar')

media = somaIdades / qtdeAlunos
print(f'a media de idades e {media} e a maior altura foi {maiorAltura}')