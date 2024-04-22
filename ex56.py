import random
numeros = list()
for i in range(20):
    numeros.append(random.randint(0, 100))

total = 0

for i in range(len(numeros)):
    total = total + numeros[i]

print(total)

contido = False
qtde = 0
for num in numeros:
    if(num == 9):
        qtde += 1
        contido = True

if(contido):
    print(f'existe {qtde} numeros 9 dentro desta lista')
else:
    print('NAO existe um 9 dentro desta lista')