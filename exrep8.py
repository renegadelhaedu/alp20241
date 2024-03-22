#vamos incrementar a questao 8 para somar e calcular a média apenas
#de números pares
acumulado = 0
qtde_pares = 0
for i in range(5):
    numero = int(input('digite um numero'))
    if(numero % 2 == 0):
        acumulado = acumulado + numero
        qtde_pares = qtde_pares + 1

if(qtde_pares == 0):
    print('nenhum numero par foi informado')
else:
    media_pares = acumulado /qtde_pares
    print(f'o valor da soma dos pares foi {acumulado} e a media foi {media_pares}')