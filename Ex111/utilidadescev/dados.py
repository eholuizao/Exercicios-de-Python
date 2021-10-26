def leiadinheiro(price):
    dado = input(price).strip().replace(",", ".")
    if dado.isalpha():
        while not dado.isnumeric():
            print(f"ERRO! \"{dado}\" é um preço inválido!")
            dado = input(price).strip().replace(",", ".")
    return float(dado)
