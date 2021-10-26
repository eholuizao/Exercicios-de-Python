soma = 0
lista = []

for x in range(1, 7):
    num = int(input("Digite um número inteiro:"))
    if num % 2 == 0:
        soma += num
        lista.append(num)
print(f"A soma dos números pares digitados {lista} igual a {soma}")
