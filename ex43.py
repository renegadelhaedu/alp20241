import random

file = open('JH.txt','w')

for i in range(20):
    idade = random.randint(18,65)
    file.write(str(idade) + '\n')
file.close()