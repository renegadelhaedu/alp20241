idade = float(input('usuario, digite sua idade'))
if(idade >= 18):
    print('voce pode fazer a prova do dentran')
    ja = idade - 18
    print(f'voce ja esta apto a fazer o teste há {ja} ano(s)')
else:
    print('voce nao pode fazer a prova pois nao tem 18 ainda')
    falta = 18 - idade
    print(f'aguarde {falta} ano(s) para voce se habilitar')
print('o programa acabou')