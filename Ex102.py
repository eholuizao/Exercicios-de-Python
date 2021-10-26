def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de um número num.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c != 1:
                print(f"{c} x", end=" ")
            else:
                print(f"{c} =", end=" ")
    return f


print(fatorial(5, show=True))
