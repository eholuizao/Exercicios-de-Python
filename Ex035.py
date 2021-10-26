l1 = float(input("Digite a medida do lado 1 do triângulo: "))
l2 = float(input("Digite a medida do lado 2 do triângulo: "))
l3 = float(input("Digite a medida do lado 3 do triângulo: "))

if (l1 + l2 > l3) and (l2 + l3 > l1) and (l1 + l3 > l2):
    print("Com esses lados, é possivel formar um triângulo.")
else:
    print("Não é possível formar um triângulo.")
