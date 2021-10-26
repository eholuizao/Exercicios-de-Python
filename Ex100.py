from random import randint


def sorteio(lista):
    print("Sorteando 5 valores da lista: ", end="")
    for c in range(1, 6):
        num = randint(1, 10)
        lista.append(num)
        print(num, end=" ")
    print("PRONTO!")


def soma(l):
    pares = 0
    for num in l:
        if num % 2 == 0:
            pares += num
    print(f"Somando os valores pares de {l}, temos {pares}")


lst = list()
sorteio(lst)
soma(lst)
