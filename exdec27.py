morangokg = float(input('digite a qtde de kilos de morango'))
macakg = float(input('digite a qtde de kilos de maca'))

if(morangokg <= 5):
    valorMorango = morangokg * 2.5
else:
    valorMorango = morangokg * 2.2

if (macakg <= 5):
    valorMaca = macakg * 2.5
else:
    valorMaca = macakg * 2.2

if(morangokg + macakg > 8 or valorMaca + valorMorango > 25):
    valorFinal = (valorMorango + valorMaca) * 0.9
else:
    valorFinal = valorMorango + valorMaca

print(f'o valor final foi {valorFinal}')



