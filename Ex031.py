dist = float(input("Digite a distância da viagem(Km): "))

if dist <= 200:
    print(f"O preço da viagem é: R${(0.5 * dist):.2f}")
else:
    print(f"O preço da viagem é: R${(0.45 * dist):.2f}")

# price = dist * 0.5 if dist <= 200 else dist * 0.45
# print(f"Preço: R${price:.2f}")
