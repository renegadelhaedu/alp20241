valor = float(input('digite o valor do produto'))

if(valor < 20):
    venda = valor * 1.45

else:
    venda = valor * 1.3

print(f'o valor da venda foi {venda}')