real = float(input("Digite um valor em reais: "))
dolar = real / 5.75
euro = real / 6.75
yene = real / 0.055

print(f'Com R${real} você pode comprar U${dolar:.2f}')
print(f'Com R${real} você pode comprar {euro:.2f} Euros')
print(f'Com R${real} você pode comprar {yene:.2f} Yenes')