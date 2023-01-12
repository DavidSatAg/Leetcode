# Resolução do problema https://leetcode.com/problems/integer-to-roman/
# Dificuldade: Média

def intToRoman(num):
    tabela = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IV'), (5, 'V'), (4, 'IV'), (1, 'I')]
    numero = []
    for i in range(len(tabela)):
        quociente = num // tabela[i][0]
        resto = num % tabela[i][0]
        num = resto
        numero.append(tabela[i][1] * quociente)
    return ''.join(numero)

print(intToRoman(3))
print(intToRoman(58))
print(intToRoman(1994))
