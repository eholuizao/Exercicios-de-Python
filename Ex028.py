from random import randint
from time import sleep

print("-=-" * 20)
print("O computador está pensando em um número...")
print("-=-" * 20)
num = randint(0, 5)

guess = int(input("Adivinhe o número (de 0 a 5): "))
print("Processando...")
sleep(3)

if guess == num:
    print("Parabéns, você acertou!")
else:
    print(f"Desculpe, você errou. O número era {num}")
