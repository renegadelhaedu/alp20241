import math

x_cz = 2
y_cz = 5
menor_dist = 9999999
nome_menor = ''
for i in range(21):
    x_city = float(input('digite o valor do eixo X da cidade'))
    y_city = float(input('digite o valor do eixo Y da cidade'))
    nome_city = input('qual o nome da cidade')

    dentro = (x_city - x_cz) + (y_city - y_cz)
    dist = math.sqrt(dentro)
    if(dist < menor_dist):
        menor_dist = dist
        nome_menor = nome_city
print(f'a cidade mais proxima e {nome_menor} que fica {menor_dist} de distancia de cz')



