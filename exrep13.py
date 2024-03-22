base = int(input('digite a base'))
exp = int(input('digite o expoente'))
resposta = 1
for i in range(exp):
    resposta = resposta * base

print(resposta)