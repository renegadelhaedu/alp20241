#questao do suspeito
p1 = input('Telefonou para a vítima?')
p2 = input('Esteve no local do crime?')
p3 = input('Mora perto da vítima?')
p4 = input('Devia para a vítima?')
p5 = input('Já trabalhou com a vítima?')
bo = 0
if(p1 == 'sim'):
    bo = bo + 1
if(p2 == 'sim'):
    bo = bo + 1
if(p3 == 'sim'):
    bo = bo + 1
if(p4 == 'sim'):
    bo = bo + 1
if(p5 == 'sim'):
    bo = bo + 1


if(bo < 2):
    print('nao tem culpa no cartorio')
if(bo == 2):
    print('suspeito')
if(bo == 3):
    print('cumplice')
if(bo == 4):
    print('cumplice')
if(bo == 5):
    print('assassino')
