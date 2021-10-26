lista = ("aprender", "programar", "aprender", "python", "curso", "gratis", "estudar", "praticar", 'praticar',
            "trabalhar", "mercado", "programador", "futuro")

for palavra in lista:
    print(f"\nNa palavra {palavra.upper()} temos as vogais: ", end="")
    for letra in palavra:
        if letra in "aeiou":
            print(letra, end=" ")
