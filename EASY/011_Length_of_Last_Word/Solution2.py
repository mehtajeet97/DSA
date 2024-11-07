# 2 While Loops method -- 1st While for removing trailing zeroes & second to calculate length of last word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        i = len(s)-1

        while i >= 0 and s[i] == ' ':
            i = i-1
        
        while i >= 0 and s[i] != ' ':
            count = count + 1
            i = i-1
        
        return count