# Versão com biblioteca math
"""
# Versão com módulo math
from math import factorial

termos = int(input("Digite ums número para calcular seu fatorial: "))

fatorial = factorial(termos)
print(f"{termos}! = {fatorial}")
"""

# Versão com while
"""
termos = int(input("Digite um número para calcular seu fatorial: "))

multiplier = termos
result = 1

print(f"{termos}! =", end=" ")
while multiplier > 0:
    print(multiplier, "x" if multiplier > 1 else "=", end=" ")
    result *= multiplier
    multiplier -= 1
print(result)
"""

# Versão com for

num = int(input("Digite um número para calcular seu fatorial: "))

multiplier = num
result = 1
print(f"{num}! =", end=" ")
for x in range(1, num + 1):
    print(multiplier, "x" if multiplier > 1 else "=", end=" ")
    result *= multiplier
    multiplier -= 1
print(result)
