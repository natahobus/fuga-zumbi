import os
import random
from jogo.mapa import criar_mapa, exibir_mapa
from jogo.jogador import mover_jogador
from jogo.zumbi import mover_zumbis

def salvar_ranking(nome, pontuacao, venceu):
    if not venceu:
        return  # Só salva quem venceu

    if not os.path.exists("dados"):
        os.makedirs("dados")

    with open("dados/ranking.txt", "a", encoding="utf-8") as f:
        f.write(f"{nome} - {pontuacao} passos\n")

def exibir_ranking():
    print("\n=== RANKING DOS JOGADORES ===")
    try:
        with open("dados/ranking.txt", "r", encoding="utf-8") as f:
            ranking = [linha.strip() for linha in f.readlines()]
            ranking.sort(key=lambda x: int(x.split('-')[1].strip().split()[0]))
            for i, linha in enumerate(ranking[:5], start=1):
                print(f"{i}º - {linha}")
    except FileNotFoundError:
        print("Nenhum ranking salvo ainda.")

def iniciar_jogo():
    print("=== FUGA DO ZUMBI ===")
    print("1. Jogar")
    print("2. Ver Ranking")
    escolha = input("Escolha uma opção: ")

    if escolha == "2":
        exibir_ranking()
        return

    tamanho = 10
    jogador = (0, 0)
    saida = (tamanho - 1, tamanho - 1)  # Saída fixa no canto inferior direito

    # Gera 10 zumbis aleatórios
    zumbis = []
    while len(zumbis) < 10:
        pos = (random.randint(0, tamanho - 1), random.randint(0, tamanho - 1))
        if pos != jogador and pos != saida and pos not in zumbis:
            zumbis.append(pos)

    nome = input("Digite seu nome: ")
    passos = 0

    while True:
        mapa = criar_mapa(tamanho, jogador, zumbis, saida)
        exibir_mapa(mapa)

        if jogador in zumbis:
            print("💀 Você foi pego pelos zumbis! Fim de jogo.")
            salvar_ranking(nome, passos, venceu=False)
            break

        if jogador == saida:
            print("🎉 Você escapou! Parabéns!")
            salvar_ranking(nome, passos, venceu=True)
            break

        direcao = input("Movimente-se (W/A/S/D): ")
        jogador = mover_jogador(jogador, direcao, tamanho)
        zumbis = mover_zumbis(zumbis, tamanho)
        passos += 1
