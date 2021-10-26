nome = input("Digite o seu nome: ")
cores = {"red": "\033[31m", "clear": "\033[m"}

# print("É um prazer te conhecer, {}".format(nome))
print(f"É um prazer te conhecer, {cores['red']}{nome}{cores['red']}!")
