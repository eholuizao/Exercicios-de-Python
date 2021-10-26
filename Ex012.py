price = float(input("Qual o preço do produto? R$:"))
prom = price - (price * 5 / 100)

print(f'O produto que custava {price:.2f}, com 5% de desconto ficará: {prom:.2f}')
