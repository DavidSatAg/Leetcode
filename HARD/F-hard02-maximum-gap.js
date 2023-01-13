// Resolução do problema https://leetcode.com/problems/maximum-gap
// Dificuldade: Fácil


var maximumGap = function(nums) {
    if (nums.length < 2) {
        return 0
    }
    let lista = []
    nums = nums.sort(function(a, b){return a - b})
    for (let i = 0; i < nums.length - 1; i++) {
        a = nums[i + 1] - nums[i]
        lista.push(a)
    }
    let maior = lista.reduce(function(a, b) {
        return Math.max(a, b)
    }, -Infinity)
    console.log(nums)
    console.log(lista)
    ;
    return maior
};


console.log(maximumGap(nums = [1, 3, 100]))
console.log(maximumGap(nums = [10]))