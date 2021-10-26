maiores = men = menores = 0
while True:
    sexo = " "
    continuar = " "

    print("CADASTRE UMA PESSOA:")
    idade = int(input("Idade: "))
    while sexo not in "MF":
        sexo = input("Sexo [M/F]").upper().strip()
    while continuar not in "SN":
        continuar = input("Quer continuar? [S/N]").upper().strip()

    if idade > 18:
        maiores += 1
    if sexo in "M":
        men += 1
    if sexo in "F" and idade < 20:
        menores += 1
    if continuar in "N":
        break

print(f"""
{maiores} pessoas maiores que 18 anos.
{men} homens cadastrados.
{menores} mulheres menores que 20 anos.""")
