def criar_mapa(tamanho, jogador_pos, zumbis_pos, saida_pos):
    mapa = [[" ." for _ in range(tamanho)] for _ in range(tamanho)]

    xj, yj = jogador_pos
    mapa[xj][yj] = "🧍"

    for zx, zy in zumbis_pos:
        mapa[zx][zy] = "🧟"

    xs, ys = saida_pos
    mapa[xs][ys] = "🏁"

    return mapa

def exibir_mapa(mapa):
    for linha in mapa:
        print(" ".join(linha))
    print()
