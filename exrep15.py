atual = 1
ant = 1
prox = 2

n = int(input('digite qual a posicao da sequencia de fibo'))

for i in range(n):
    prox = atual + ant
    ant = atual
    atual = prox
print(atual)