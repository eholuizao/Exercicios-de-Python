import math

num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = math.sqrt(num)

cores = {"clear": "\033[m",
         "white": "\033[4;30m",
         "blue": "\033[1;30;44m",
         "ciano": "\033[1;30;46m",
         "roxo": "\033[1;30;45m"}

print(f"""
O número escolhido foi: {cores['white']}{num}{cores['clear']}
\033[34mSeu dobro é {cores['blue']} {dobro} {cores['clear']}
\033[36mSeu triplo é {cores['ciano']} {triplo} {cores['clear']}
\033[35mSua raiz é {cores['roxo']} {raiz:.2f} {cores['clear']}
""")
