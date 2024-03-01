idade = int(input('digite sua idade'))
valor_carteira = float(input('digite quanto vc tem na carteira'))

if(idade >= 18 or valor_carteira >= 50):
    print('vc pode entrar')
else:
    print('vc nao pode entrar')