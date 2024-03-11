ano = str(input('digite o ano'))
terminazero = ano[:-2] != '00'
if(terminazero and int(ano) % 4 == 0):
    print('bissexto')
else:
    print('nao e bissexto')