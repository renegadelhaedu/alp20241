todosSalarios = 0
op = -1
contador = 0
while(op != 0):

    print('\nMENU')
    print('1-Inserir salario')
    print('2-Calcular media salarial')
    print('0-Sair')

    op = int(input('digite a opcao desejada '))

    if(op == 1):
        salario = float(input('digite seu salario'))
        todosSalarios = todosSalarios + salario
        contador = contador + 1
    elif(op == 2):
        if(contador == 0):
            print('nenhum salario foi informado')
        else:
            media = todosSalarios / contador
            print(f'a media dos salarios ate agora e {media}')
    else:
        print('opcao invalida')