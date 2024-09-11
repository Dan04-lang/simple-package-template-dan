from PIL import Image, ImageFilter

def carregar_imagem(caminho):
    return Image.open(caminho)

def salvar_imagem(imagem, caminho):
    imagem.save(caminho)

def aplicar_filtro(imagem):
    return imagem.filter(ImageFilter.BLUR)
