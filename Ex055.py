lista = []

for x in range(1, 6):
    peso = float(input(f"Digite o seu peso da pessoa {x}: "))
    lista.append(peso)

print(f"O maior peso foi: {max(lista)}kg \no menor peso foi: {min(lista)}kg")

# Resolução GUANABARA
'''
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}° pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}kg')
print(f'O menor peso lido foi {menor}kg')
'''
