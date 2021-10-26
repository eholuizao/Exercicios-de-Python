lista = []

while True:
    cont = " "
    num = int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
    else:
        print("Esse número já tem na lista.")
    while cont not in "SsNn":
        cont = input("Quer continuar? [S/N]")
    if cont in "Nn":
        break
lista.sort()
print(f"Você digitou os valores: {lista}")
