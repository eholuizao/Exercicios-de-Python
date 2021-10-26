first = int(input("Digite o primeiro termo da P.A: "))
razao = int(input("Digite a razão da P.A: "))

c = 0
mais = 10
total = 0
while mais != 0:
    total += mais
    while c < total:
        print(first, end=" ")
        first += razao
        c += 1
    print("PAUSA")
    mais = int(input("Digite quantos termos você quer a mais?"))

print(f"FIM! {total} termos no total.")
