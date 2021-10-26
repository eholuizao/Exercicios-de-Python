from random import randint

tupla = ()
for c in range(0, 5):
    tupla2 = (randint(1, 10),)
    tupla += tupla2

print(f"""{tupla}
menor valor: {min(tupla)}
maior valor: {max(tupla)}""")
