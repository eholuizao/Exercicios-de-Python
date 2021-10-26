num = int(input('Digite um número entre 0 e 9999: '))
num2 = str(10000 + num)
print(f"Analisando o número {num}...")
print(f"""Unidade: {num2[4]}
Dezenas: {num2[3]}
Centenas: {num2[2]}
Milhar: {num2[1]}""")

