#digite as 3 notas do aluno e o sistema deve calcular se ela está
#aprovado (maior igual a 7), reprovado (menor que 4) ou na final (meio termo)
n1 = float(input('digite a nota da primeira prova'))
n2 = float(input('digite a nota da segunda prova'))
n3 = float(input('digite a nota da terceira prova'))

media = (n1 + n2 + n3) /3

if(media >= 7):
    print('parabens. vc foi aprovado')
if(media >= 4 and media < 7):
    print('na final. vai certo. confio em vc')
if(media < 4 ):
    print('proximo semestre vc tenta novamente')





