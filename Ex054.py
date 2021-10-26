from datetime import date
atual = date.today().year
lista = []

#Cria a lista das 7 idades
for x in range(1, 8):
    nasc = int(input(f"Digite o ano de nascimento da pessoa {x}:"))
    idade = atual - nasc
    lista.append(idade)

#Identifica quais idades da lista são maiores/iguais que 18
maior = 0
menor = 0
for x in range(0, 7):
    if lista[x] >= 18:
        maior += 1
    else:
        menor += 1

print(f"Dessas 7 pessoas, {maior} estão acima dos 18 e {menor} estão abaixo.")

# Versão GUANABARA
'''
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}° pessoa nasceu?'))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'Ao todo tivemos {totmenor] pessoas menores de idade')
'''