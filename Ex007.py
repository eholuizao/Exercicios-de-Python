nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

if media >= 7:
    print(f'A média entre {nota1} e {nota2} é igual a {media:.1f}. \033[32mVocê passou!!!')
else:
    print(f'A média entre {nota1} e {nota2} é igual a {media:.1f}. \033[31mVocê reprovou...')
