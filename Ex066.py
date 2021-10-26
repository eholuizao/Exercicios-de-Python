lista = []
n = 0
while True:
    n = int(input("Digite um número inteiro (999 para parar): "))
    if n == 999:
        break
    lista.append(n)

print(f"Quantidade de números digitados: {len(lista)} \nSoma entre todos os números: {sum(lista)}")
