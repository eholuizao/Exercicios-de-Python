frase = str(input("Digite uma frase: ")).strip().lower()

anum = frase.count("a")
fpos = frase.find("a") + 1
lpos = frase.rfind("a") + 1


print(f"""A letra A aparece {anum} vezes na frase. 
A primeira letra A aparece na posição: {fpos}
A última letra A aparece na posição: {lpos}""")
