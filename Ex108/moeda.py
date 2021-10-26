def metade(price):
    return price / 2


def dobro(price):
    return price * 2


def aumentar(price, taxa):
    res = price + (price * (taxa/100))
    return res


def diminuir(price, taxa):
    res = price - (price * (taxa/100))
    return res


def moeda(price, unity="R$"):
    return f"{unity}{price:>.2f}".replace('.', ',')
