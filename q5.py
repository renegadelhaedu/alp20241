sb = float(input('digite seu salario bruto'))
prest = float(input('digite o valor da prestacao'))

if(prest > 0.3 * sb):
    print('nao tem direito a credito')
else:
    print('emprestimo concedido')