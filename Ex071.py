valor = int(input("Qual valor você quer sacar? R$"))
count50 = count20 = count10 = count1 = 0

while valor >= 50:
    valor -= 50
    count50 += 1
while valor >= 20:
    valor -= 20
    count20 += 1
while valor >= 10:
    valor -= 10
    count10 += 1
while valor >= 1:
    valor -= 1
    count1 += 1

print(f"Total de {count50} cédulas de R$50") if count50 >= 1 else False
print(f"Total de {count20} cédulas de R$20") if count20 >= 1 else False
print(f"Total de {count10} cédulas de R$10") if count10 >= 1 else False
print(f"Total de {count1} moedas de R$1") if count1 >= 1 else False
