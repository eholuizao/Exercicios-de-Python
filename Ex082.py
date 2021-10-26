lista = []
pares = []
impares = []

while True:
    cont = " "
    num = int(input("Digite um valor: "))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

    while cont not in "SsNn":
        cont = input("Você quer continuar? [S/N]")
    if cont in "Nn":
        break

print(f"Lista original: {lista}")
print(f"Números pares: {pares}")
print(f"Números impares {impares}")
