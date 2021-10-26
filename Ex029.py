vel = int(input("Digite a velocidade atual do carro: "))
multa = 7 * (vel - 80)

if vel > 80:
    print(f"Você foi multado. Valor: R${multa:.2f}")
else:
    print("Tenha um bom dia, dirija com segurança.")