from math import hypot

cat1 = int(input("Digite o valor do primeiro cateto: "))
cat2 = int(input("Digite o valor do segundo cateto: "))
hyp = hypot(cat1, cat2)

print(f"A hipotenusa desse triângulo mede: {hyp}")