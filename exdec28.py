litros = float(input('digite a quantidade'))
tipo = input('digite A-alcool ou G-gasolina')

if(tipo == 'A' and litros <= 20):
    valor = litros * (1.9 * 0.97)
elif(tipo == 'A' and litros > 20):
    valor = litros * (1.9 * 0.95)
elif(tipo == 'G' and litros <= 20):
    valor = litros * (2.5 * 0.96)
elif(tipo == 'G' and litros > 20):
    valor = litros * (2.5 * 0.94)
else:
    valor = 0
    print('voce escolheu o combustivel errado')

print(f'voce vai pagar {valor} reais')
