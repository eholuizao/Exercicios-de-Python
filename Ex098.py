from time import sleep


def repete(ini, fim, pulo):
    if pulo < 0:
        print(f"Contagem de {ini} até {fim} de {-pulo} em {-pulo}")
        for x in range(ini, fim - 1, pulo):
            sleep(0.3)
            print(x, end=" ")
    elif fim > ini:
        print(f"Contagem de {ini} até {fim} de {pulo} em {pulo}")
        for x in range(ini, fim + 1, pulo):
            sleep(0.3)
            print(x, end=" ")
    elif ini > fim:
        print(f"Contagem de {ini} até {fim} de {pulo} em {pulo}")
        for x in range(ini, fim - 1, -pulo):
            sleep(0.3)
            print(x, end=" ")
    print("FIM!")
    print("=-" * 30)


repete(1, 10, 1)
repete(10, 0, 2)
print("Agora é sua vez de personalizar a contagem!")
i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: "))
repete(i, f, p)
