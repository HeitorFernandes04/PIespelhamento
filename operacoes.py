import numpy as np


def adicionar(f, g):
    media = (f.astype(np.float64) + g.astype(np.float64)) / 2
    return media.astype(np.uint8)


def subtrair(f, g):
    diferenca = f.astype(np.float64) - g.astype(np.float64)
    minimo, maximo = diferenca.min(), diferenca.max()
    escalada = (diferenca - minimo) / (maximo - minimo) * 255
    return escalada.astype(np.uint8)


def espelhar(f):
    return f[:, ::-1]