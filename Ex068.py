from random import randint
vitorias = 0

while True:
    parimp = " "
    num = int(input("Diga um valor: "))
    while parimp not in "PI":
        parimp = input("Par ou impar? [P/I]").upper().strip()
    comp = randint(0, 10)
    soma = num + comp

    if soma % 2 == 0:
        result = "P"
        if parimp == result:
            print(f"Sua jogada: {parimp} \nJogada do computador: {comp}")
            print(f"A soma dos números é {soma}, um número Par, você ganhou! \nVamos jogar de novo...")
            vitorias += 1
        else:
            print(f"Sua jogada: {parimp} \nJogada do computador: {comp}")
            print(f"A soma dos números é {soma}, um número Par, você perdeu.")
            break
    else:
        result = "I"
        if parimp == result:
            print(f"Sua jogada: {parimp} \nJogada do computador: {comp}")
            print(f"A soma dos números é {soma}, um número Impar, você ganhou! \nVamos jogar de novo...")
            vitorias += 1
        else:
            print(f"Sua jogada: {parimp} \nJogada do computador: {comp}")
            print(f"A soma dos números é {soma}, um número Impar, você perdeu.")
            break
print(f"GAME OVER! Total de vitórias: {vitorias}")
