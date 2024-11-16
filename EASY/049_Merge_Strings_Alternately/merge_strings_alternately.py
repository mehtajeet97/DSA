class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #Create two pointers and array
        i,j = 0,0
        res = []
        # Iterate through both words and input each char into result array
        while i<len(word1) and j<len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i = i+1
            j = j+1
        # Append all remaining characters 
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)