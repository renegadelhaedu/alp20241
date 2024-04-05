maior = 0
menor = 999999999

for i in range(5):
    n = int(input('digite um numero'))

    if(n < menor):
        menor = n

    if(n > maior):
        maior = n

print(f' {maior} e {menor}')
