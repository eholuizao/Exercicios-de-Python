from random import randint
from time import sleep

print("Adivinhe o número que o computador pensou.")
guess = int(input("Digite um valor de (1 a 10): "))
pc = randint(1, 10)
erros = 0

while guess != pc:
    print("Processando. . .")
    sleep(1.5)
    if guess > pc:
        guess = int(input("Menos, Tente novamente: "))
    elif guess < pc:
        guess = int(input("Mais, tente novamente:"))
    erros += 1

print("Processando. . .")
sleep(1.5)
print(f"Você acertou! \nQuantidade de erros: {erros}")
