class Solution:
    def validPalindrome(self, s: str) -> bool:
        # Create two pointer left and right
        l, r = 0, len(s)-1
        # Check left char and right char is equal
        while l < r:
            if s[l] != s[r]:
            # If not, check substrings are equal
                skipL, skipR = s[l+1 : r+1], s[l:r]
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            l = l+1
            r = r-1
        return True