# Check through Two hashmaps for bijection (both ways)

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        
        hashc2w = {}
        hashw2c = {}
        for c, w in zip(pattern, words):
            if c in hashc2w and hashc2w[c] != w :
                return False

            if w in hashw2c and hashw2c[w] != c :
                return False
            
            hashc2w[c] = w
            hashw2c[w] = c
        return True