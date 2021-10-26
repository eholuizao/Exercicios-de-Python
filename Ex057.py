sexo = input("Digite seu sexo: [M/F]").upper().strip()

while sexo not in "MF" or sexo == "":
    sexo = input("Dados inválidos, digite seu sexo novamente: [M/F]").upper().strip()
print(f"Sexo {sexo} registrado com sucesso.")
