from PIL import Image

imagem = Image.open('C:/Users/rnsg/Desktop/fotorene2.png')

largura = imagem.size[0]
altura = imagem.size[1]

lista_vermelho = []
lista_verde = []
lista_azul = []

for x in range(largura):
    for y in range(altura):

        pixel_rgb = imagem.getpixel((x, y))
        vermelho, verde, azul = pixel_rgb

        lista_vermelho.append(vermelho)
        lista_verde.append(verde)
        lista_azul.append(azul)

media_vermelho = sum(lista_vermelho) / len(lista_vermelho)
media_verde = sum(lista_verde) / len(lista_verde)
media_azul = sum(lista_azul) / len(lista_azul)


print("vermelho:", media_vermelho)
print("verde:", media_verde)
print("azul:", media_azul)