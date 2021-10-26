valor = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual o seu salário? R$"))
anos = int(input("Quantos anos vai financiar? R$"))

mensal = valor / (anos * 12)
minimo = salario * 0.30

if mensal > minimo:
    print(f"Pra pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${mensal:.2f}")
    print("EMPRESTIMO NEGADO!")
else:
    print(f"Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de R${mensal:.2f}")
    print("EMPRESTIMO APROVADO!")
