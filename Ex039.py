from datetime import date
atual = date.today().year
nasc = int(input("Ano de nascimento: "))
idade = atual - nasc

if idade == 18:
    print("Já é hora de se alistar!")
elif idade > 18:
    print(f"Já passou do tempo de se alistar, você está {idade - 18} anos atrasado.")
    print(f"Seu alistamento foi em {atual - (idade - 18)}")
else:
    print(f"Você ainda vai se alistar, falta apenas {18 - idade} anos.")
    print(f"Seu alistamento será em {atual + (18 - idade)}")
