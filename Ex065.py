lista = []
num = int(input("Digite um número inteiro(999 para parar): "))
while num != 999:
    lista.append(num)
    num = int(input("Digite um número inteiro(999 para parar): "))

print(f"Foram digitados {len(lista)} números e a soma entre eles é igual a: {sum(lista)}")
