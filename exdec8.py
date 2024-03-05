p1 = float(input('digite o valor'))
p2 = float(input('digite o valor'))
p3 = float(input('digite o valor'))

if(p1 < p2 and p1 < p3):
    print('voce deve comprar o produto1')

if(p2 < p1 and p2 < p3):
    print('voce deve comprar o produto2')

if(p3 < p2 and p3 < p1):
    print('voce deve comprar o produto3')