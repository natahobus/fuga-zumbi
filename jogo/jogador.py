def mover_jogador(posicao, direcao, tamanho):
    x, y = posicao

    movimentos = {
        "W": (-1, 0),
        "S": (1, 0),
        "A": (0, -1),
        "D": (0, 1)
    }

    if direcao.upper() not in movimentos:
        return posicao

    dx, dy = movimentos[direcao.upper()]
    novo_x, novo_y = x + dx, y + dy

    if 0 <= novo_x < tamanho and 0 <= novo_y < tamanho:
        return (novo_x, novo_y)

    return posicao
