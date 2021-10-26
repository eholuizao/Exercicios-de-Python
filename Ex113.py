def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO! Digite um número inteiro válido!")
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("ERRO! Digite um número decimal válido!")
            continue  # Retorna ao começo do while.
        else:
            return n


num1 = leiaInt("Digite um número inteiro: ")
num2 = leiaFloat("Digite um número decimal: ")
print(f"O número inteiro digitado foi: {num1} e o número decimal foi: {num2}")
