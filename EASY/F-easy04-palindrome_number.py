# Resolução do problema https://leetcode.com/problems/palindrome-number/
# Dificuldade: Fácil


def isPalindrome(x: int) -> bool:
    if str(x) == str(x)[::-1]:
        return True
    else: 
        return False


print(isPalindrome(x = 121))
print(isPalindrome(x = -121))
print(isPalindrome(x = 10))
