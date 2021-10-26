# Solução sem listas
"""
expressao = input("Digite sua expressão matemática: ")

pilha = 0
for caracter in expressao:
    if caracter in "(":
        pilha += 1
    if caracter in ")":
        pilha -= 1
    if pilha < 0:
        break
if pilha == 0:
    print("Sua expressão é válida!")
else:
    print("Sua expressão é inválida!")
"""

expressao = input("Digite sua expressão matemática: ")

pilha = []
for caracter in expressao:
    if caracter in "(":
        pilha.append(caracter)
    elif caracter in ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(caracter)
            break
if len(pilha) == 0:
    print("Expressão válida!")
else:
    print("Expressão inválida!")
