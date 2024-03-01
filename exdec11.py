sal = float(input('digite seu salario'))

if(sal <= 280):
    aumento = sal * 0.2
    perc = 20
if(sal > 280 and sal <= 700):
    aumento = sal * 0.15
    perc = 15
if(sal > 700 and sal <= 1500):
    aumento = sal * 0.1
    perc = 10
if(sal > 1500):
    aumento = sal * 0.05
    perc = 5

sal_final = sal + aumento
print(f'voce ganhava {sal} e agora ganhara {sal_final}')
print(f'seu salario teve um aumento de {perc}% que em reais foi {aumento}')