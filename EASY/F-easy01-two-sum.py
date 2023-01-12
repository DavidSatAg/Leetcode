# Resolução do problema https://leetcode.com/problems/two-sum/
# Dificuldade Fácil


def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                return [i, j]


# def twoSum(nums, target):
#     passed = {}
#     for index,num in enumerate(nums):
#         rest = target - num

#         if(rest in passed):
#             return [index, passed[rest]]
        
#         passed[num] = index


print(twoSum(nums = [2,7,11,15], target = 9))
print(twoSum(nums = [3,2,4], target = 6))
print(twoSum(nums = [3,3], target = 6))