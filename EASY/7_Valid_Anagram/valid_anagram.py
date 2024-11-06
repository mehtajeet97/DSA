# Sorting Method : If strings are anagrams then their sorted version should be the same
# Time : O(nlogn)
# Space : O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t): return True
        return False
