//  Resolução do problema https://leetcode.com/problems/two-sum/
// Dificuldade: Fácil


var twoSum = function(nums, target) {
    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < nums.length; j++) {
            if ((nums[i] + nums[j] == target) && i != j) {
                return [i, j]
            }
        }
    }
};


console.log(twoSum(nums = [2,7,11,15], target = 9))