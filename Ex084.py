pessoas = []
dados = []
pesos = []

while True:
    cont = " "
    dados.append(input("Digite o seu nome: "))
    dados.append(float(input("Digite o seu peso(kg): ")))
    pessoas.append(dados[:])
    pesos.append(dados[1])
    dados.clear()
    while cont not in "SsNn":
        cont = input("Você quer continuar? [S/N]: ")
    if cont in "Nn":
        break

print(f"Ao todo, você cadastrou {len(pessoas)} pessoas")
print(f"O maior peso foi de {max(pesos)}kg. Peso de: ", end="")
for p in pessoas:
    if p[1] == max(pesos):
        print(f"[{p[0]}]", end=" ")
print(f"\nO menor peso foi de {min(pesos)}kg. Peso de: ", end="")
for p in pessoas:
    if p[1] == min(pesos):
        print(f"[{p[0]}]", end=" ")
