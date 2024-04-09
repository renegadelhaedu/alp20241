soma = 0
qtde  = 0
for p in range(90):

    nome = input('digite seu nome')
    nota = float(input('digite sua media'))

    if(nome == 'fim'):
        break
    else:
        soma = nota + soma
        qtde = qtde + 1

media = soma / qtde
