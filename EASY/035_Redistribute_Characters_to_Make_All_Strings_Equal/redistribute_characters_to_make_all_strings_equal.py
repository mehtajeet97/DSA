from typing import List
from collections import defaultdict

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        # Create default dictionary
        charCount = defaultdict(int)

        # Count occurrence of each character in all words
        for w in words:
            for c in w:
                charCount[c] += 1
        
        # Check character count is not divisible by Array length
        for c in charCount:
            if charCount[c] % len(words):
                return False
        
        return True