a = float(input('digite o valor'))
if(a == 0):
    print('essa equacao nao e de segundo grau')
else:
    b = float(input('digite o valor'))
    c = float(input('digite o valor'))

    delta = (b**2) - 4*a*c
    if(delta < 0):
        print('nao possui raizes reais')
    if(delta == 0):
        x = -b + (delta ** (1/2))
        print(f'o valor da unica raiz e {x}')
    if(delta > 0):
        x1 = (-b + delta ** (1/2)) / (2*a)
        x2 = (-b - delta ** (1/2)) / (2*a)
        print(f'as raizes sao {x1} e {x2}')

