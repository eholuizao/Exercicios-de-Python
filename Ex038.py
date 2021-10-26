num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

if num1 > num2:
    print(f"O primeiro número é maior que o segundo ({num1} > {num2})")
elif num1 < num2:
    print(f"O segundo número é maior que o primeiro ({num1} < {num2})")
else:
    print(f"Os dois valores são iguais!")
