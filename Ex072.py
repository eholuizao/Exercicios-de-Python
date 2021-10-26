numeros = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito", "Nove", "Dez", "Onze", "Doze",
           "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
userNum = int(input("Digite um número de 0 a 20 para ver ele em extenso: "))

while not 0 <= userNum <= 20:
    userNum = int(input("Digite um número de 0 a 20 para ver ele em extenso: "))

print(f"{userNum} - {numeros[userNum]}")
