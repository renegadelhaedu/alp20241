texto = input('digite seu nome completo')
qtde = 0
for letra in texto:
    if(letra != ' '):
        qtde = qtde + 1

print(f'seu nome possui {qtde} letras')