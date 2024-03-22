inicio = int(input('digite o inicio do intervalo'))
final = int(input('digite o final do intervalo'))
soma = 0
for num in range(inicio, final + 1):
    soma = soma + num

print(soma)