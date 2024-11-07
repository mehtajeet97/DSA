# strip method removes any leading/trailing whitespaces and then reverse iteration is used to find the length of last word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        x = s.strip()

        for i in range(len(x) - 1, -1, -1): 
            if x[i] != " ": 
                length += 1
            else:  
                break
        
        return length
