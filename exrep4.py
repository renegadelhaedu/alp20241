popA = 80000
popB = 200000
txA = 1.03
txB = 1.015
qtde_anos = 0
for i in range(15):
    popA *= txA
    popB *= txB
popA = int(popA)
popB = int(popB)
print(f'A:{popA} e B:{popB}')
'''
while(popB > popA):
    qtde_anos += 1
    popA *= txA
    popB *= txB

print(f'levaram {qtde_anos} anos para A ultrapassar B')

'''

