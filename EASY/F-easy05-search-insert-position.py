# Resolução do problema https://leetcode.com/problems/search-insert-position/
# Dificuldade: Fácil


def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        nums.sort()
        return nums.index(target)


print(searchInsert(nums = [1,3,5,6], target = 5))
print(searchInsert(nums = [1,3,5,6], target = 2))
print(searchInsert(nums = [1,3,5,6], target = 7))