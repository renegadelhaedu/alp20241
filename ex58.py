p = [ ['rene',12,1.67],['toinho',26,2.1],['babi',17,1.9],['sed',23,2] ]

for i in range(len(p)):
    if(p[i][1] < 18):
        p[i][0] = p[i][0] + ' representado pelo responsavel'

for pessoa in p:
    print(pessoa)


