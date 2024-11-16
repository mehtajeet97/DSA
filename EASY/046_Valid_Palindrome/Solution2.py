class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create two pointers left & right
        l, r = 0, len(s)-1

        # Compare each character on the left is equal to right
        while l < r:
            while l<r and not self.isAlphaNum(s[l]):
                l += 1
            while r>l and not self.isAlphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            l = l+1
            r = r-1
        return True
        
    # Handle Upper case and Alphanumeric
    def isAlphaNum(self, c):
            return (ord('A')<=ord(c)<=ord('Z') or 
            (ord('a')<=ord(c)<=ord('z')) or 
            (ord('0')<=ord(c)<=ord('9')))