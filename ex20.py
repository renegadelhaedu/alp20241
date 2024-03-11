import random

num = random.randint(1, 100)
chute = int(input('chute um numero entre 1 e 100 '))
if(num == chute):
    print('vc e uma pessoa de sorte')
else:
    if(chute < num):
        chute = int(input('chute um valor maior'))
        if(chute == num):
            print('caba de sorte. acertou!')
        else:
            print('errou de novo. o numero era ', num)
    else:
        chute = int(input('chute um valor menor'))
        if(chute == num):
            print('caba de sorte. acertou!')
        else:
            print('errou de novo. o numero era ', num)
