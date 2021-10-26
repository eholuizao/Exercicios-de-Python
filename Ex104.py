def leiaInt(msg):
    num = input(msg)
    while not num.isnumeric():
        print("ERRO! Digite um número inteiro válido!")
        num = input(msg)
    return int(num)


# Programa Principal
n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")
