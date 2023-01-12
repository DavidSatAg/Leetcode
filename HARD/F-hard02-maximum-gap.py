# Resolução do problema https://leetcode.com/problems/maximum-gap/
# Dificuldade: Difícil


def maximumGap(nums):
    if len(nums) < 2:
        return 0
    lista = []
    nums = sorted(nums)
    for i in range(len(nums) - 1):
        a = abs(nums[i + 1] - nums[i])
        lista.append(a)
    maior = max(lista)
    return maior


print(maximumGap(nums = [3,6,9,1]))