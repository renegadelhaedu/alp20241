l1 = int(input('digite um lado'))
l2 = int(input('digite um lado'))
l3 = int(input('digite um lado'))

if(l1 == l2 and l2 == l3):
    print('triangulo equilatero')

if(l1 != l2 and l2 != l3 and l1 != l3):
    print('triangulo escaleno')

if((l1 == l2 and l1 != l3) or (l1 == l3 and l1 != l2) or (l2 == l3 and l2 != l1)):
    print('triangulo isosceles')