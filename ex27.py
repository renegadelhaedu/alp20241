nome1 = 'cadeyra'
nome2 = 'cadeira'
equivalente = True
for ind in range(7):
    if(nome1[ind] != nome2[ind]):
        equivalente = False

if(equivalente):
    print('sao iguais')
else:
    print('sao diferentes')