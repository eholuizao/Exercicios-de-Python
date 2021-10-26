num = int(input("Digite um número inteiro:"))
option = int(input("""Escolha um número:
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL
"""))

if option == 1:
    print(f"O número {num} em binário é {bin(num)[2:]}")
elif option == 2:
    print(f"O número {num} em octal é {oct(num)[2:]}")
elif option == 3:
    print(f"O número {num} em hexadecimal é {hex(num)[2:]}")
else:
    print(f"Opção inválida, tente novamente.")
