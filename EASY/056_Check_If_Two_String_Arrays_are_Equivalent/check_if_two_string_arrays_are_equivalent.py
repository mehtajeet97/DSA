# Optimum Solution with Space complexity

from typing import List
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Create Four Pointers
        # Two pointers for index of words
        w1 = w2 = 0 
        # Two pointers for index of chars
        i = j = 0

        while w1<len(word1) and w2 < len(word2):
            # Check for mismatch
            if word1[w1][i] != word2[w2][j]:
                return False
            i = i+1
            j = j+1

            if i == len(word1[w1]):
                w1 = w1+1
                i = 0

            if j == len(word2[w2]):
                w2 = w2+1
                j = 0
        
        # Check if any words remain in either after loop exited
        if w1 < len(word1) or w2 < len(word2):
            return False

        return True