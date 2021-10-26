num1 = input('Digite um número:')
num2 = input('Digite outro número:')
soma = int(num1) + int(num2)

cores = {"limpa": "\033[m",
         "red": "\033[31m",
         "green": "\033[32m",
         "yellow": "\033[33m",
         "blue": "\033[34m"}

print(f'A soma de {cores["red"]}{num1}{cores["limpa"]} e'
      f' {cores["blue"]}{num2}{cores["limpa"]} é: {cores["yellow"]}{soma}{cores["limpa"]}')
