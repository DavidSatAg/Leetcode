# Resolução do problema https://leetcode.com/problems/maximum-score-words-formed-by-letters/
# Dificuldade: Difícil


from itertools import combinations, chain
from collections import Counter


def maxScoreWords(words, letters, score):
    lista_letras = []
    palavras_possiveis = []
    combinacoes = list(chain.from_iterable(combinations(words, r) for r in range(len(words) + 1)))
    for subconjunto in combinacoes:
        palavra = ""
        for i in subconjunto:
            palavra += i
        lista_letras = []
        for letra in palavra:
            lista_letras.append(letra)
            lista_letras.sort()
        check = Counter(letters) >= Counter(lista_letras)
        if check:
            palavras_possiveis.append(lista_letras)
    lista_valores = []
    breakpoint()
    for i in palavras_possiveis:
        soma = 0
        for letra in i:
            soma += score[ord(letra) - 97]
        lista_valores.append(soma)
    maior = max(lista_valores)
    return maior

print(maxScoreWords(words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))
print(maxScoreWords(words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]))
print(maxScoreWords(words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]))





# Recebemos lista de palavras, letras e pontuação de cada letra
# devemos retornar uma soma da pontuação de um conjnto de palavras da lista possíveis de serem montadas com as letras. 


# primeiro podemos fazer uma lista de de conjunto de palavra possíveis
    # para isso podemos fazer todas as combinações possíveis  
# Depois somamos a pontuação de cada conjunto e fazemos uma lista com ela
# Depois vemos qual é a maior pontuação