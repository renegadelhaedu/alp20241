#leia o nome do usuario e mostre na tela o nome lido sem as vogais

nome = input('digite seu nome')

for le in nome:
    if(le != 'a' and le != 'e' and le != 'i' and le != 'o' and le != 'u' ):
        print(le)