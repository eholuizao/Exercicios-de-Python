l1 = float(input("Digite o primeiro lado do triângulo: "))
l2 = float(input("Digite o segundo lado do triângulo: "))
l3 = float(input("Digite o terceiro lado do triângulo: "))

# Checa se é possível formar um triângulo
if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print("É possível formar um triângulo!")

    # Checa se o triângulo é equilátero/escaleno/isósceles caso seja possível forma-lo.
    if l1 == l2 == l3:
        print("O triângulo é EQUILÁTERO.")
    # Se l1 for diferente de l2 e l2 for diferente de l3, que por sua vez for diferente de l1 = escaleno
    elif l1 != l2 != l3 != l1:
        print("O triângulo é ESCALENO")
    else:
        print("O triângulo é ISÓSCELES")
else:
    print("Não é possível formar um triângulo!")
