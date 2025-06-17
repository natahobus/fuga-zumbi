import random

def mover_zumbis(zumbis, tamanho):
    novas_posicoes = []
    for zx, zy in zumbis:
        dx, dy = random.choice([(-1,0), (1,0), (0,-1), (0,1), (0,0)])
        novo_x = max(0, min(tamanho-1, zx + dx))
        novo_y = max(0, min(tamanho-1, zy + dy))
        novas_posicoes.append((novo_x, novo_y))
    return novas_posicoes
