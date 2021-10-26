from datetime import date
atual = date.today().year
trabalhador = {"nome": input("Nome: ").title(),
               "idade": atual - int(input("Ano de nascimento: ")),
               "ctps": int(input("Carteira de trabalho(0 não tem): "))}

if trabalhador["ctps"] != 0:
    trabalhador["salário"] = float(input("Salário: R$"))
    trabalhador["contratação"] = int(input("Ano de contratação: "))
    trabalhador["aposentadoria"] = trabalhador["idade"] + (trabalhador["contratação"] + 35) - atual

for k, v in trabalhador.items():
    print(f"{k} tem o valor {v}")
