num = int(input("Digite um número inteiro: "))
continuar = input("Você quer continuar? [S/N]: ").upper().strip()

# Lista de todos os valores que vão ser digitados
lista = [num]

while continuar not in "N":
    if continuar not in "SN":
        continuar = input("Valor inválido, digite novamente [S/N]: ").upper().strip()
    else:
        num = int(input("Digite outro número inteiro:"))
        lista.append(num)
        continuar = input("Você quer continuar? [S/N]: ").upper().strip()

media = sum(lista) / len(lista)
print(f"""
A média entre todos os elementos da lista é: {media}
O maior número digitado foi: {max(lista)}
O menor número digitado foi: {min(lista)}""")
