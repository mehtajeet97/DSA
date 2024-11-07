class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = 0
        og = x
        while x > 0 :
            y = y*10 + int(x%10)
            x=int(x/10)
        if (og == y):
            return True
        return False