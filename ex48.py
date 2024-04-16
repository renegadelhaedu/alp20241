op = ''

while(op != 'sair'):

    print('1-inserir nota de usuario')
    print('2-calcular media')
    print('sair')

    op = input('digite a opcao desejada ')

    if(op == '1'):
        alunos = open('alunos.txt', 'a')
        notas = open('notas.txt', 'a')

        nome = input('digite seu nome ')
        nota = float(input('digite sua nota'))
        while( nota < 0 or nota > 10):
            nota = float(input('digite sua nota novamente de forma correta'))

        alunos.write('\n' + nome)
        notas.write('\n' + str(nota))
        alunos.close()
        notas.close()

    elif(op == '2'):
        notas = open('notas.txt', 'r')
        linhas = notas.readlines()
        soma = 0
        qtde_numeros = 0
        for line in linhas:
            if(line != '\n'):
                soma += float(line)
                qtde_numeros += 1

        notas.close()

        media = round(soma / qtde_numeros, 2)
        print(f'a media das notas e {media}')

