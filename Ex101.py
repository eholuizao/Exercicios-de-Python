def voto(y):
    from datetime import date
    idade = date.today().year - y
    if 18 <= idade <= 70:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"
    elif idade > 70 or 16 <= idade < 18:
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: NÃO VOTA"


ano = int(input("Ano de nascimento: "))
print(voto(ano))
