price = float(input("Digite o preço do produto: R$"))
pagamento = int(input("""
Digite 1 para à vista dinheiro/cheque
Digite 2 para à vista no cartão
Digite 3 para até 2x no cartão
Digite 4 para 3x ou mais no cartão
"""))

if pagamento == 1:
    total = price - (price * 0.10)
elif pagamento == 2:
    total = price - (price * 0.05)
elif pagamento == 3:
    total = price
    parcela = total / 2
    print(f"Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS")
elif pagamento == 4:
    qparcel = int(input("Quantas parcelas?"))
    total = price + (price * 0.20)
    parcela = total/qparcel
    print(f"Sua compra será parcelada em {qparcel}x de R${parcela:.2f} COM JUROS")
else:
    total = price
    print("Não identificamos seu pagamento, tente novamente!")
print(f"Sua compra de R${price} vai custar R${total} no final.")
