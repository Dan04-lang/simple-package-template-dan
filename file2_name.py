from file1_name import carregar_imagem, salvar_imagem, aplicar_filtro

def processar_imagem(caminho_entrada, caminho_saida):
    imagem = carregar_imagem(caminho_entrada)
    imagem_processada = aplicar_filtro(imagem)
    salvar_imagem(imagem_processada, caminho_saida)

if __name__ == "__main__":
    caminho_entrada = 'input.jpg'  # Exemplo de caminho de entrada
    caminho_saida = 'output.jpg'   # Exemplo de caminho de saída
    processar_imagem(caminho_entrada, caminho_saida)
