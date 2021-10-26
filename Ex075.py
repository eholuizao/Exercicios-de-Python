tupla = ()
for x in range(1, 5):
    tupla2 = (int(input("Digite um valor: ")),)
    tupla += tupla2

quant9 = tupla.count(9)
pos3 = tupla.index(3) if 3 in tupla else False
listaPares = []

for num in tupla:
    if num % 2 == 0:
        listaPares.append(num)

print(f"Você digitou os números: {tupla}")
print(f"O número nove aparece {quant9} vezes.")
print(f"A primeira vez que o número três aparece foi na {pos3 + 1}° posição.")
print(f"Números pares digitados: {listaPares}")
