num = int(input("Digite o número de termos de fibonacci que você quer ver: "))

f1 = 0
f2 = 1

cont = 0
while cont <= num:
    cont += 1
    f3 = f1 + f2
    f1 = f2
    f2 = f3
    print(f1, end=" ")
