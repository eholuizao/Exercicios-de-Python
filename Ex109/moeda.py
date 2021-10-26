def metade(price, formata=False):
    """
    @param price: Valor a ser passado.
    @param formata: Formata para um valor monetário usando a função "moeda()". (Padrão=False)
    @return: Retorna a metade do valor.
    """
    return moeda(price/2) if formata else price/2


def dobro(price, formata=False):
    """
    @param price: Valor a ser passado.
    @param formata: Formata para um valor monetário usando a função "moeda". (Padrão=False)
    @return: Retorna o dobro do valor
    """
    return moeda(price*2) if formata else price*2


def aumentar(price, taxa, formata=False):
    """
    @param price: Valor a ser passado.
    @param taxa: Percentual da taxa aplicada sobre o valor.
    @param formata: Formata para um valor monetário usando a função "moeda". (Padrão=False)
    @return: Retorna o valor aumentado taxa%.
    """
    res = price + (price * (taxa/100))
    return moeda(res) if formata else res


def diminuir(price, taxa, formata=False):
    """
    @param price: Valor a ser passado.
    @param taxa: Percentual da taxa aplicada sobre o valor.
    @param formata: Formata para um valor monetário usando a função "moeda". (Padrão=False)
    @return: Retorna o valor diminuido taxa%.
    """
    res = price - (price * (taxa/100))
    return moeda(res) if formata else res


def moeda(price, unity="R$"):
    """
    @param price: Valor a ser passado.
    @param unity: Unidade monetária. (Padrão="R$")
    @return: Retorna o valor formatado.
    """
    return f"{unity}{price:>.2f}".replace('.', ',')
