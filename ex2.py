s0 = int(input('digite o deslocamento inicial'))
vin = int(input('digite a velocidade inicial'))
t = int(input('digite o tempo gasto'))
ace = int(input('digite o valor da aceleracao '))

final = s0 + vin * t + ((ace*(t*t))/2)

print(f'o valor final da MRUV foi {final}')