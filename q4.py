sm = float(input('digite o saldo medio'))

if(sm <= 500):
    credito = 0
elif(sm <= 1000):
    credito = sm * 0.3
elif(sm <= 3000):
    credito = sm * 0.4
else:
    credito = sm * 0.5

print(f'para o seu saldo medio de {sm}, o credito aprovado foi {credito}')