for numero in range(3, 5000):
    qtde = 0
    for i in range(2, numero):
        if(numero % i == 0):
            qtde = qtde + 1
    if(qtde == 0):
        print(f'{numero} eh primo')
