def area(larg, comp):
    print(f"A área de um terreno {larg}x{comp} é de {larg * comp:.1f}m²")


area(float(input("Digite a largura: ")), float(input("Digite o comprimento: ")))
