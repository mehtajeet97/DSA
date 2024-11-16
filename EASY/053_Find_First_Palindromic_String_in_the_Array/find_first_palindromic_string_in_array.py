from typing import List

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        #Use two pointers to find palindrome
        for w in words:
            l,r = 0, len(w)-1
            while w[l] == w[r]:
                if l>=r:
                    return w
                l = l+1
                r = r-1
        return ""