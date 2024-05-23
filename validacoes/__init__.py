
def validar_capacidade(texto):
    campo = int(input(texto))
    while (campo < 0):
        campo = int(input(texto))
    return campo

def validar_valor(texto):
    campo = float(input(texto))
    while (campo < 0):
        campo = float(input(texto))
    return campo

def validar_campo(texto):

    campo = input(texto)
    while(len(campo) == 0):
        campo = input(texto)
    return campo
