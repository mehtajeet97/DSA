class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): #For edge cases of x being negative number, or single digit
            return False
        revertedNumber = 0
        while x > revertedNumber: # Divides it equally
            revertedNumber = revertedNumber * 10 + x % 10  
            x //= 10    #Integer Division
        return x == revertedNumber or x == revertedNumber // 10 # Condition after OR for ODD numbers