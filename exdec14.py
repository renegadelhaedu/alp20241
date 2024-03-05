n1 = float(input('digite sua primeira nota'))

n2 = float(input('digite sua segunda nota'))

soma = (n1 + n2)/2

if(soma >= 9):
    print('A')

if(soma >= 7.5 and soma < 9):
    print('B')

if(soma >= 6 and soma < 7.5):
    print('C')

if(soma >= 4 and soma < 6):
    print('D')

if(soma < 4):
    print('E')