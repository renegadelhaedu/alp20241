n1 = int(input('digite um numero'))
n2 = int(input('digite um numero'))
n3 = int(input('digite um numero'))

if(n1 > n2 and n2 > n3):
    print(f'{n1} {n2} {n3}')
if(n1 > n3 and n3 > n2):
    print(f'{n1} {n3} {n2}')
if(n2 > n1 and n1 > n3):
    print(f'{n2} {n1} {n3}')
if(n2 > n3 and n3 > n1):
    print(f'{n2} {n3} {n1}')
if(n3 > n2 and n2 > n1):
    print(f'{n3} {n2} {n1}')
if(n3 > n1 and n1 > n2):
    print(f'{n3} {n2} {n1}')