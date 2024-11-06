# Sorting Method : If strings are anagrams then their sorted version should be the same

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t): return True
        return False
