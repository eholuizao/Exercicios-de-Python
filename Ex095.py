jogadores = []

while True:
    cont = " "
    dic = {'nome': input("Digite o nome do jogador: "), 'gols': []}
    partidas = int(input("Quantas partidas ele jogou? "))
    for c in range(1, partidas + 1):
        dic['gols'].append(int(input(f"Quantos gols na partida {c}? ")))
    jogadores.append(dic.copy())
    while cont not in "SsNn":
        cont = input("Quer continuar? [S/N]")
    if cont in "Nn":
        break

print("-=" * 30)
print(f"{'cod':<2} {'nome':<10} {'gols':<20} {'total'}")
print("-" * 60)
for pos, d in enumerate(jogadores):
    print(f"{pos:>2} {d['nome']!s:<12} {d['gols']!s:<20} {sum(d['gols'])}")

while True:
    num = int(input("Mostrar dados de qual jogador? (999 pra parar): "))
    if num == 999:
        break
    print(f"-- LEVANTAMENTO DO JOGADOR {jogadores[num]['nome']}")
    for pos, d in enumerate(jogadores):
        if num >= len(jogadores):
            print("ERRO! Esse jogador não existe!")
        else:
            for p, gol in enumerate(d['gols']):
                print(f"Na partida {p + 1} ele fez {gol} gols.")
print("<< VOLTE SEMPRE >>")
