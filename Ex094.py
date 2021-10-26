lista = []
soma = 0

while True:
    dic = {'nome': input("Nome: ").title(),
           'idade': int(input("Idade: ")),
           'sexo': input("Sexo [M/F]: ").upper()}
    while dic['sexo'] not in "MmFf":
        print("ERRO! Digite apenas M ou F.")
        dic['sexo'] = input("Sexo [M/F]: ").upper()
    lista.append(dic.copy())

    cont = input("Quer continuar? [S/N]")
    while cont not in "SsNn":
        print("ERRO! Responda apenas S ou N.")
        cont = input("Quer continuar? [S/N]")
    if cont in "Nn":
        break

for d in lista:
    soma += d['idade']
print("-=" * 30)
print(f"A) Ao todo, temos {len(lista)} pessoas cadastradas.")
print(f"B) A média de idade é {soma/len(lista):.2f} anos")
print(f"C) As mulheres cadastradas foram ", end="")
for d in lista:
    if d['sexo'] in "Ff":
        print(d['nome'], end=" ")
print()
print(f"D) Lista de pessoas que estão acima da média:")
for d in lista:
    for k, v in d.items():
        print(f"{k} = {v};", end=" ")
    print()
print("<< ENCERRADO >>")
