print("=" * 20 + "ANALISADOR DE TEXTO" + "=" * 20)

nome = str(input("Digite seu nome: ")).strip()
nospace = nome.replace(" ", "")
# nospace = len(nome) - nome.count(" ")
# splitnome = nome.split()

uper = nome.upper()
lower = nome.lower()
nlength = len(nospace)
fnlength = nome.find(" ")
# fnlength = len(splitnome[0])

print(f"""
Nome em maiúsculas: {uper}
Nome em minúsculas: {lower}
N° de letras: {nlength}
N° de letras do primeiro nome: {fnlength}
""")
