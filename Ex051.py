first = int(input("Digite o primeiro termo da PA:"))
razao = int(input("Digite a razão da PA:"))
decimo = first + (10 - 1) * razao

for x in range(first, decimo + 1, razao):
    print(x, end=" ")
