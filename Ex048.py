soma = 0
quant = 0

for x in range(1, 501, 2):
    if x % 3 == 0:
        quant += 1
        soma += x
print(f"A soma de todos os números ímpares({quant} valores) que são múltiplos de 3, entre 1 e 500 é igual a: {soma}")
