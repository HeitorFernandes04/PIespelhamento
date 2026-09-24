import sys

import numpy as np
from PIL import Image, ImageDraw

from operacoes import adicionar, subtrair, espelhar


def gerar_ruidosa(imagem, intensidade=8):
    ruido = np.random.normal(0, intensidade, imagem.shape)
    ruidosa = imagem.astype(np.float64) + ruido
    return np.clip(ruidosa, 0, 255).astype(np.uint8)


def gerar_com_marca(imagem):
    com_marca = Image.fromarray(imagem).copy()
    desenho = ImageDraw.Draw(com_marca)
    largura, altura = com_marca.size
    raio = min(largura, altura) // 6
    cx, cy = largura // 2, altura // 2
    desenho.ellipse([cx - raio, cy - raio, cx + raio, cy + raio], fill=255)
    return np.array(com_marca)


def main():
    if len(sys.argv) != 2:
        print("uso: python3 main.py foto.jpg")
        return

    original = np.array(Image.open(sys.argv[1]).convert("L"))

    ruidosa = gerar_ruidosa(original)
    media = adicionar(ruidosa, gerar_ruidosa(original))

    com_marca = gerar_com_marca(original)
    diferenca = subtrair(com_marca, original)

    espelhada = espelhar(original)

    Image.fromarray(original).show(title="original")
    Image.fromarray(ruidosa).show(title="uma copia ruidosa")
    Image.fromarray(media).show(title="adicao: media de duas copias ruidosas")
    Image.fromarray(com_marca).show(title="copia com marca")
    Image.fromarray(diferenca).show(title="subtracao: so a marca sobra")
    Image.fromarray(espelhada).show(title="espelhamento")

    Image.fromarray(media).save("resultado_adicao.png")
    Image.fromarray(diferenca).save("resultado_subtracao.png")
    Image.fromarray(espelhada).save("resultado_espelhamento.png")
    print("resultados salvos: resultado_adicao.png, resultado_subtracao.png, resultado_espelhamento.png")


if __name__ == "__main__":
    main()
