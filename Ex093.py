jogador = {"nome": input("Nome do jogador: ").title(), "gols": []}
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

for c in range(0, partidas):
    jogador["gols"].append(int(input(f"  Quantos gols na partida {c}?")))
jogador["total"] = sum(jogador["gols"])

print("=-" * 30)
print(jogador)
print("=-" * 30)

for k, v in jogador.items():
    print(f"O campo {k} tem valor {v}")
print("=-" * 30)

print(f"O jogador {jogador['nome']} jogou {partidas} partidas")
for pos, g in enumerate(jogador["gols"]):
    print(f"Na partida {pos}, fez {g} gols")
print(f"Foi um total de {jogador['total']} gols.")
