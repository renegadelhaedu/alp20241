num = int(input('digite um numero inteiro para calculo de fatorial'))

fatorial = 1
for i in range(1, num + 1):
    fatorial = fatorial * i

print(f'o fatorial de {num} e fatorial {fatorial}')