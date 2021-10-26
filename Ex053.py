# Minha versão: Sem for e tira os acentos tbm

from unidecode import unidecode
frase = input("Digite uma frase: ").lower().replace(" ", "")
# tira os acentos da string
noaccent = unidecode(frase)
lista = list(noaccent)
# reverte a lista
reverso = lista[::-1]

if lista == reverso:
    print("A frase é um palindromo")
else:
    print("A frase não é um palindromo")


# Versão com for(GUANABARA):
'''
frase = input("Digite uma frase: ").strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(junto, inverso)
if inverso == junto:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
'''

