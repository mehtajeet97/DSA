# Reverse Iteration Method & removal of trailing zeroes by splitting

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for c in range(len(s)-1, -1, -1):
            if s[len(s)-1] == ' ':
                s = s[:-1]
            else:
                if s[c] != ' ':
                    count = count+1
                else:
                    break
        return count
