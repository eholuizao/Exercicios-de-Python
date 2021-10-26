total = maiorqMil = menorV = cont = 0
maisBarato = ""
while True:
    produto = input("Digite o nome do produto: ")
    valor = float(input("Digite o preço do produto: R$"))
    continuar = " "
    cont += 1

    total += valor
    if valor > 1000:
        maiorqMil += 1
    if cont == 1 or valor < menorV:
        maisBarato = produto
        menorV = valor

    while continuar not in "SN":
        continuar = input("Você quer continuar? [S/N]").upper().strip()
    if continuar == "N":
        break

print(f"""
O valor total da compra foi R${total:.2f}
Temos {maiorqMil} produtos custando mais que R$1000.00
O produto mais barato foi {maisBarato} custando R${menorV:.2f}""")
