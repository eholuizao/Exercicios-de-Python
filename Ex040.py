nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
media = (nota1 + nota2) / 2

if media < 5:
    print(f"REPROVADO! MÉDIA: {media:.1f}")
elif 7 > media > 5:
    print(f"ESTÁ DE RECUPERAÇÃO! MÉDIA: {media:.1f}")
else:
    print(f"APROVADO! MÉDIA: {media:.1f}")