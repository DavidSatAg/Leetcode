# Resolucação do problema https://leetcode.com/problems/smallest-even-multiple/ 
# Dificuldade: Fácil


def smallestEvenMultiple(n: int):
    if n % 2 != 0:
        return n * 2
    return n


print(smallestEvenMultiple(n = 5))
print(smallestEvenMultiple(n = 6))