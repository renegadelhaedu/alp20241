linf = int(input('digite o limite inferior'))
lsup = int(input('digite o limite superior'))
mult = int(input('digite o valor que deseja encontrar os multiplos'))

for i in range(linf + 1, lsup):
    if(i % mult == 0):
        print(i)
