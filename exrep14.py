pares = 0
impares = 0

for num in range(10):
    numero = int(input('digite um numero qualqer'))

    if(numero % 2 == 0):
        pares = pares + 1
    else:
        impares = impares + 1

print(f'a quantidade de pares foi {pares}')
print(f'a quantidade de impares foi {impares}')