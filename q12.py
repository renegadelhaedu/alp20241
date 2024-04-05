qtde =int(input('digite a quantidade de numeros que devem ser lidos'))

menor = 99999999
maior = -99999999

for x in range(qtde):
    numero = int(input('digite um numero'))

    if(numero < menor):
        menor = numero

    if(numero > maior):
        maior = numero

print(f'o menor foi {menor} e o maior foi {maior}')
