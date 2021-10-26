x = input("Digite algo:")
cores = {"branco": "\033[1;30m", "clear": "\033[m"}

text = f"""
O tipo primitivo desse valor é: {cores['branco']}{type(x)}{cores['clear']}
Só tem espaços? {x.isspace()}
É um número? {x.isnumeric()}
É alfabético? {x.isalpha()}
É alfanumérico? {x.isalnum()}
Está apenas em maiúsculas? {x.isupper()}
Está apenas em minúsculas? {x.islower()}
Está capitalizada? {x.istitle()}"""

# Bota o true de cor verde coco e bota false de vermelho ne papae
if "True" in text:
    text = text.replace("True", "\033[1;32m True \033[m")
if "False" in text:
    text = text.replace("False", "\033[1;31m False \033[m")
print(text)
