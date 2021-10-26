lista = []
for x in range(1, 6):
    num = int(input(f"Digite o {x}° valor: "))
    if x == 1 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print(lista)
