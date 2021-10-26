lista_idade = []
maioridadeH = 0
Hmaisvelho = ''
totM = 0

for x in range(1, 5):
    print(f"{x}° PESSOA")
    nome = input("Nome: ").strip().title()
    idade = int(input("Idade: "))
    lista_idade.append(idade)
    sexo = input("Sexo [M/F]: ").strip().upper()

    if x == 1 and sexo == "M":
        maioridadeH = idade
        Hmaisvelho = nome
    if sexo == "M" and idade > maioridadeH:
        maioridadeH = idade
        Hmaisvelho = nome
    if sexo == "F" and idade < 20:
        totM += 1

# media das idades da lista
media = sum(lista_idade) / len(lista_idade)

print(f"A média de todas as idades é: {media}")
print(f"O homem mais velho tem {maioridadeH} anos e se chama {Hmaisvelho}")
print(f"Ao todo são {totM} mulheres com menos de 20 anos.")
