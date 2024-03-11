import random
sousa_ataque = random.randint(1, 10)
sousa_defesa = random.randint(1, 10)

petro_ataque = random.randint(1, 10)
petro_defesa = random.randint(1, 10)

valor_final = (sousa_defesa - petro_ataque) + int((sousa_ataque - petro_defesa) * 1.2)
if(valor_final == 0):
    print('Sousa e petrolina empatam sem gols no marizao')
elif(valor_final > 0 ):
    print('Sousa humilha o petrolina e Danilo Bala metralha no marizao')
    print(f'Petrolina {(sousa_defesa - petro_ataque) * -1} x {int((sousa_ataque - petro_defesa) * 1.2)} Sousa')
else:
    print('Petrolina surpreende o Sousa em casa e torcida invade o campo')
    print(f'Petrolina {(sousa_defesa - petro_ataque)*-1} x {int((sousa_ataque - petro_defesa) * 1.2)} Sousa')


