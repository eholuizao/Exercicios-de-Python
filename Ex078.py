lista = []

for x in range(1, 6):
    val = int(input("Digite um valor: "))
    lista.append(val)

maior = max(lista)
menor = min(lista)

print(f"""
{lista}
O menor valor digitado foi: {menor} e sua posição é {lista.index(menor)}
O maior valor digitado foi: {maior} e sua posição é {lista.index(maior)}""")
