from time import sleep
num1 = int(input("Digite o 1° valor: "))
num2 = int(input("Digite o 2° valor: "))
end = False
while end is False:
    menu = int(input(f"""
[ 1 ] Somar {num1} + {num2}
[ 2 ] Multiplicar {num1} * {num2}
[ 3 ] Maior entre {num1} e {num2}
[ 4 ] Novos números
[ 5 ] Sair"""))
    if menu == 5:
        print("Finalizando...")
        sleep(1.5)
        end = True
    elif menu == 1:
        print(f"A soma entre {num1} e {num2} é: {num1 + num2}")
    elif menu == 2:
        print(f"O produto entre {num1} e {num2} é {num1 * num2}")
    elif menu == 3:
        lista = [num1, num2]
        print(f"O maior número entre {num1} e {num2} é: {max(lista)}")
        if num1 == num2:
            print("Os 2 números são iguais.")
    elif menu == 4:
        num1 = int(input("Digite novamente o 1° número"))
        num2 = int(input("Digite novamente o 2° número"))
    else:
        print("Valor invalido, tente novamente:")
        menu = int(input(f"""[ 1 ] Somar {num1} + {num2}
[ 2 ] Multiplicar {num1} * {num2}
[ 3 ] Maior entre {num1} e {num2}
[ 4 ] Novos números
[ 5 ] Sair"""))
