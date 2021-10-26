larg = float(input("Digite a largura da parede: "))
alt = float(input("Digite a altura da parede: "))

area = larg * alt
tinta = area / 2

print(f'Sua parede tem dimensão {larg}x{alt} e sua área é de {area}m² '
      f'\nPara pintar essa parede, você precisará de {tinta}L de tinta')