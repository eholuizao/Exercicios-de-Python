altura = float(input("Digite a altura em m: "))
peso = float(input("Digite o peso em kg: "))
imc = peso / (altura ** 2)

print(f"O IMC dessa pessoa é {imc:.1f}")
if imc < 18.5:
    print("Abaixo do Peso.")
elif imc < 25:
    print("Peso Ideal.")
elif imc < 30:
    print("Sobrepeso.")
elif imc < 40:
    print("Obesidade.")
elif imc >= 40:
    print("Obesidade mórbida.")
