matriz = [[], [], []]
somap = soma3c = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f"Adicione um valor a posição [{l}, {c}] da matriz: ")))

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()

for l in matriz:
    for num in l:
        if num % 2 == 0:
            somap += num
        if l.index(num) == 2:
            soma3c += num
print(f"A soma de todos os valores pares da matriz é: {somap}")
print(f"O maior valor da segunda linha é: {max(matriz[2])}")
print(f"A soma de todos os valores da terceira coluna é: {soma3c}")
