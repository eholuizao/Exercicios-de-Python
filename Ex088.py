from random import randint
from time import sleep
lista = []
temp = []

jogos = int(input("Quantos jogos você quer que eu sorteie? "))

for x in range(1, jogos + 1):
    quant = 0
    while quant < 6:
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
        quant += 1
    temp.sort()
    lista.append(temp[:])
    temp.clear()

for pos, jogo in enumerate(lista):
    print(f"Jogo {pos + 1}: {jogo}")
    sleep(1)
