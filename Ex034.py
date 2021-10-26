salario = float(input("Digite o seu salário: "))

if salario > 1250:
    aumento = salario + (salario * 10)/100
    print(f"Quem ganhava R${salario}, passa a ganhar R${aumento:.2f} agora.")
else:
    aumento = salario + (salario * 15)/100
    print(f"Quem ganhava R${salario}, passa a ganhar R${aumento:.2f} agora.")
