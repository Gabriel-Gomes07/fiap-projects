import random

opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura", 4: "Lagarto", 5: "Spock"}

vitorias = {
    1: {3: "quebra", 4: "esmaga"},
    2: {1: "cobre",  5: "refuta"},
    3: {2: "corta",  4: "decapita"},
    4: {2: "come",   5: "envenena"},
    5: {1: "vaporiza", 3: "derrete"},
}

testes = [(5, 1), (3, 5), (2, 2)]

for jogador, computador in testes:
    print(f"Você: {opcoes[jogador]}")
    print(f"Computador: {opcoes[computador]}")

    if jogador == computador:
        print("Empate!")
    elif computador in vitorias[jogador]:
        acao = vitorias[jogador][computador]
        print(f"{opcoes[jogador]} {acao} {opcoes[computador]} — Você venceu!")
    else:
        acao = vitorias[computador][jogador]
        print(f"{opcoes[computador]} {acao} {opcoes[jogador]} — Computador venceu!")

    print()