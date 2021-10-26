num = int(input('Digite um número: '))
suc = num + 1
ant = num - 1
cores = {"clear": "\033[m", "blue": "\033[1;34m", "ciano": "\033[1;36m", "roxo": "\033[1;35m"}

print(f'O número escolhido foi {cores["blue"]}{num}{cores["clear"]},'
      f'seu sucessor é {cores["roxo"]}{suc}{cores["clear"]} e seu antecessor é {cores["ciano"]}{ant}{cores["clear"]}')
