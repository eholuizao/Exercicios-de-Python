"""
val1 = int(input("Digite o valor 1: "))
val2 = int(input("Digite o valor 2: "))
val3 = int(input("Digite o valor 3: "))

# Menor
menor = val1
if val2 < val1 and val2 < val3:
    menor = val2
if val3 < val1 and val3 < val2:
    menor = val3

print(f"Menor valor: {menor}")

# Maior
maior = val1
if val2 > val1 and val2 > val3:
    maior = val2
if val3 > val1 and val3 > val2:
    maior = val3

print(f"Maior valor: {maior}")
"""

val1 = int(input("Digite o valor 1: "))
val2 = int(input("Digite o valor 2: "))
val3 = int(input("Digite o valor 3: "))

lista = [val1, val2, val3]
lista.sort()

print(f"""Menor valor: {lista[0]} 
Maior valor: {lista[2]}""")
