def jogador(nome, gols):
    if not gols.isnumeric():
        gols = 0
    if nome.isspace() or not nome:
        nome = "<desconhecido>"
    return f"O jogador {nome} fez {gols} gol(s) no campeonato."


n = input("Nome do jogador: ")
g = input("Número de gols no campeonato: ")
print(jogador(n, g))
