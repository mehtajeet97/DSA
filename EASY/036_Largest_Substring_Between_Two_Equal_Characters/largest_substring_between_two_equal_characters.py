class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        #Create Character Mapping to the first occurence Index
        characterIndex={}
        res = -1

        #Check the second occurence and subtract the first index from map
        for i,c in enumerate(s):
            if c in characterIndex:
                res = max(res, i - characterIndex[c] - 1)
            else:
                characterIndex[c] = i
        
        return res