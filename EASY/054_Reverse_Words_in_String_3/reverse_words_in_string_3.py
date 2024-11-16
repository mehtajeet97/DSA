class Solution:
    def reverseWords(self, s: str) -> str:
        # String is single unit, convert it to array(List)
        s = list(s)
        # Create two pointers left and right
        l = 0
        for r in range(len(s)):
        # When right reaches whitespace reverse the substring using pointers
            if s[r] == " " or r == len(s)-1:
                tempL, tempR = l, r-1
        # For last word, ensure right does not go out of bounds    
                if r == len(s)-1:
                    tempR = r

                while tempL < tempR:
                    s[tempL], s[tempR] = s[tempR], s[tempL]
                    tempL = tempL+1
                    tempR = tempR-1
            
                l = r+1

        return ''.join(s)
        