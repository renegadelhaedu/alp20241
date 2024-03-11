import yfinance as yf

dados = yf.Ticker('USDBRL=X').history()
dolar = float(dados['Close'][-1])
opcao = int(input('digite 1 para converter dolar para real ou 2 o contrario'))

if(opcao == 1):
    valor = float(input('digite o valor em dolar'))
    convertido = valor * dolar
    convertido = round(convertido, 2)
    print(f'o valor em reais e R$ {convertido}')
elif(opcao == 2):
    valor = float(input('digite o valor em reais'))
    convertido = valor / dolar
    convertido = round(convertido, 2)
    print(f'o valor em dolares e $ {convertido}')
else:
    print('voce digitou a opcao invalida e o programa vai encerrar')