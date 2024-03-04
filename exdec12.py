qtdehr = int(input('digite a qtde de horas trabalhadas no mes'))
valorhr = float(input('digite o valor da sua hora de trabalho'))

sal_bruto = qtdehr * valorhr

if(sal_bruto <= 900):
    ir = 0
if(sal_bruto > 900 and sal_bruto <= 1500):
    ir = 5/100
if(sal_bruto > 1500 and sal_bruto <= 2500):
    ir = 10/100
if(sal_bruto > 2500):
    ir = 20/100

valor_ir = (sal_bruto * ir)
sal_liq = sal_bruto - valor_ir

inss = sal_liq * 0.1
fgts = sal_liq * 0.11
total_descontos = inss + fgts + valor_ir
valor_final = sal_liq - inss
print(f'o salario bruto foi: {sal_bruto}')
print(f'o IR {valor_ir} e o salario liquido {sal_liq}')
print(f'inss:{inss} - fgts:{fgts} ')
print(f'no final ele recebeu apenas {valor_final}')
