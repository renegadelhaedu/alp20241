alunos = {}
disciplinas = dict()

for i in range(5):
    mat = input('digite sua matricula')
    nome = input('digite seu nome')

    alunos[mat] = nome

for i in range(3):
    nomeDic = input('digite o nome da disciplina')
    cod = input('digite o code da disciplina')

    disciplinas[cod] = [nomeDic, alunos]



