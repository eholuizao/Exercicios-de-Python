from time import sleep
from random import choice
janken = str(input("Pedra, papel ou tesoura?")).strip().lower()
lista = ["pedra", "papel", "tesoura"]
pcjanken = choice(lista)

print("PEDRA")
sleep(1)
print("PAPEL")
sleep(1)
print("TESOURA")

if janken not in "pedra papel tesoura":
    print("Desculpe, não entendemos.")
elif janken == "pedra" and pcjanken == "tesoura":
    print("Você venceu!")
    print(f"Sua escolha: {janken}, escolha do pc: {pcjanken}")
elif janken == "papel" and pcjanken == "pedra":
    print("Você venceu!")
    print(f"Sua escolha: {janken}, escolha do pc: {pcjanken}")
elif janken == "tesoura" and pcjanken == "papel":
    print("Você venceu!")
    print(f"Sua escolha: {janken}, escolha do pc: {pcjanken}")
elif janken == pcjanken:
    print("Empate!")
    print(f"Sua escolha: {janken}, escolha do pc: {pcjanken}")
else:
    print("Você perdeu.")
    print(f"Sua escolha {janken}, escolha do pc: {pcjanken}")
