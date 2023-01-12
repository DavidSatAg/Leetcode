# Resolução do problema https://leetcode.com/problems/letter-combinations-of-a-phone-number
# Dificuldade: Média


def letterCombinations(digits):
    tabela = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    lista = []
    for i in digits:
        lista.append(tabela[i])
    combinacoes = []
    if len(lista) == 1:
        return lista[0]
    try:
        for i in lista[0]:
            for j in lista[1]:
                for k in lista[2]:
                    for l in lista[3]:
                        a = [i, j, k, l]
                        combinacoes.append(a)
    except:
        try:
            for i in lista[0]:
                for j in lista[1]:
                    for k in lista[2]:
                        a = [i, j, k]
                        combinacoes.append(a)
        except:
            try:
                for i in lista[0]:
                    for j in lista[1]:
                            a = [i, j]
                            combinacoes.append(a)
            except:
                return []
    for i in range(len(combinacoes)):
        combinacoes[i] = ''.join(combinacoes[i])
    return combinacoes


print(letterCombinations(digits="23"))
print(letterCombinations(digits=""))
print(letterCombinations(digits="2"))
print(letterCombinations(digits="234"))
print(letterCombinations(digits="2345"))
