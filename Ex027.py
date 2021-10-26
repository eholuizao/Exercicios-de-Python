nome = input("Digite seu nome: ").title().strip().split()

print(f"""Muito prazer te conhecer!
Seu primeiro nome é {nome[0]}
Seu último nome é {nome[-1]}""")  # ou len(nome) - 1
