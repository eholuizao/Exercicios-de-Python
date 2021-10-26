numeros = [[], []]

for x in range(1, 8):
    num = int(input(f"Digite o {x}° valor: "))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f"Valores pares digitados: {numeros[0]} \nValores impares digitados: {numeros[1]}")
