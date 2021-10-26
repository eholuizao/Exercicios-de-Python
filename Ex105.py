def notas(* n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    @param n: uma ou mais notas dos alunos (aceita várias)
    @param sit: valor opcional, indicando se deve ou não mostrar a situação.
    @return: dicionário com várias informações sobre a situação da turma.
    """
    dic = {'total': len(n), 'maior': max(n), 'menor': min(n), 'media': round(sum(n)/len(n), 2)}
    if sit:
        if dic['media'] >= 7:
            dic['situação'] = "BOA"
        elif dic['media'] >= 5:
            dic['situação'] = "RAZOÁVEL"
        else:
            dic['situação'] = "RUIM"
    return dic


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
