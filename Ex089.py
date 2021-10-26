lista = []

while True:
    cont = " "
    nome = (str(input("Nome: ")))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])

    while cont not in "SsNn":
        cont = input("Quer continuar? [S/N]")
    if cont in "Nn":
        break

print("-=" * 30)
print(f"{'No.':<4}{'NOME':<10}{'MEDIA':>8}")
print("-" * 30)
for pos, aluno in enumerate(lista):
    print(f"{pos:<4} {aluno[0].title():<10} {aluno[2]:>8.1f}")

while True:
    print("-" * 30)
    num = int(input("Mostrar notas de qual aluno? (999 p parar) No: "))
    if num == 999:
        break
    if num <= len(lista) - 1:
        print(f"Notas de {lista[num][0]}: {lista[num][1]}")
    else:
        print("Aluno não identificado.")
