num = int(input("Digite um número inteiro: "))
tot = 0

for i in range(1, num + 1):
    if num % i == 0:
        print("\033[33m", end=" ")
        tot += 1
    else:
        print("\033[34m", end=" ")
    print(i, end=" ")

print(f"\033[m\nO número {num} foi divisível por {tot} número(s)")
if tot == 2:
    print("Por isso ele é PRIMO")
else:
    print("Por isso ele NÃO é primo")
