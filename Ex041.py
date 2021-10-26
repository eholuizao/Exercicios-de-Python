from datetime import date
atual = date.today().year
ano = int(input("Qual o ano de nascimento do nadador?"))
idade = atual - ano

print(f"O atleta tem {idade} anos.")
if idade <= 9:
    print("Nadador Mirim.")
elif idade <= 14:
    print("Nadador Infantil")
elif idade <= 19:
    print("Nadador Júnior")
elif idade == 20:
    print("Nadador Sênior")
else:
    print("Nadador Master")
