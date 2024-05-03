jogadoras = {12:['julia',19,{'ataque':87, 'defesa':56}],
             11:['jordanna',18,{'ataque':82, 'defesa':77}],
            15:['gabrielle',17,{'ataque':89, 'defesa':67}],
            17:['vitoria',22,{'ataque':62, 'defesa':97}],
             }
while(True):
    print('1-adicionar jogadora')
    print('2-listar melhores defensoras')
    print('3-listar melhores atacantes')
    print('4-atualizar jogadora')
    print('5-listar jogadores maiores de 17 que são boas defensoras')
    print('6-remover as jogadoras que não sao boas defensoras')
    print('7-remover2 as jogadoras que não sao boas defensoras')
    print('8-listar todas jogadoras')
    print('0-sair')
    op = input('digite a opcao desejada')

    if(op == '1'):
        cod = int(input('digte o codigo da jogadora'))
        nome = input('digite o nome')
        idade = int(input('digite sua idade'))
        ataq = int(input('digite o valor do ataque desta jogadora'))
        defe = int(input('digite o valor de defesa desta jogadora'))

        jogadoras[cod] = [nome, idade, {'ataque':ataq, 'defesa':defe}]
    elif(op == '2'):
        for chave in jogadoras:
            if (jogadoras[chave][2]['defesa'] > 70):
                print('\n-----Lista das melhores defensoras')
                print(jogadoras[chave][0])
    elif(op == '3'):
        for chave in jogadoras:
            if (jogadoras[chave][2]['ataque'] > 70):
                print('\n-----Lista das melhores atacantes')
                print(jogadoras[chave][0])
    elif(op == '4'):
        cod = int(input('informe o codigo da jogadora'))
        ataq = int(input('digite o valor do ataque desta jogadora'))
        defe = int(input('digite o valor de defesa desta jogadora'))

        jogadoras[cod][2]['ataque'] = ataq
        jogadoras[cod][2]['defesa'] = defe
    elif(op == '5'):
        for chave in jogadoras:
            if(jogadoras[chave][1] > 17 and jogadoras[chave][2]['defesa'] >= 70):
                print(jogadoras[chave][0])

    elif(op == '6'):
        rem = []
        for chave in jogadoras:
            if(jogadoras[chave][2]['defesa'] < 70):
                rem.append(chave)

        for codjogadora in rem:
            jogadoras.pop(codjogadora)

    elif(op == '7'):
        busca = input('digite o nome da jogadora que vc esta procurando')
        for chave in jogadoras:
            if(busca in jogadoras[chave][0]):
                print(f'{chave} - {jogadoras[chave][0]}')
        codRem = int(input('digite o codigo da jogadora que vc quer remover'))
        if(codRem in jogadoras):
            jogadoras.pop(codRem)
        else:
            print('meu lindo, vc digitou um codigo invalido')

    elif(op == '8'):
        for chave in jogadoras:
            print(f'{chave} - {jogadoras[chave][0]}')

    elif(op == '0'):
        break

