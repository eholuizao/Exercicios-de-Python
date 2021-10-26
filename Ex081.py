lista = []

while True:
    cont = " "
    num = int(input("Digite um valor: "))
    lista.append(num)
    while cont not in "SsNn":
        cont = input("Vocêr quer continuar? [S/N]: ")
    if cont in "Nn":
        break
lista.sort(reverse=True)
print(f"Foram digitados {len(lista)} números da ordem decrescente: {lista}")
print("Existe o valor 5 na lista.") if 5 in lista else print("Não existe o valor 5 na lista")
