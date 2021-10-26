def linha(msg):
    print("~" * 30)
    print(msg)
    print("~" * 30)


def ajuda(chave):
    from time import sleep
    linha(f"Acessando o manual de {chave}...")
    sleep(1.5)
    help(chave)


while True:
    linha("Sistema de ajuda pyHelp")
    k = input("Função ou biblioteca:")
    if k.upper() == "FIM":
        linha("Até logo!")
        break
    ajuda(k)
