from typing import List
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # Checking reverse word
        for w in words:
            if w == w[::-1]:
                return w
        return ""