# Basic Solution -- Bad space complexity
from typing import List
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Create two empty strings
        str1, str2 = '', ''

        # Iterate through each array and concatenate each into string initialized
        for n in word1:
            str1 += n
        
        for n in word2:
            str2 += n
        
        # Compare Strings
        if str1 == str2:
            return True
        else:
            return False