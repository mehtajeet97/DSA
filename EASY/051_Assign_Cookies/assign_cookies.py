from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort the input arrays
        g.sort()
        s.sort()
        # Compare smallest (first values) in both arrays with two pointers
        i = j = 0

        while i<len(g):
            while j < len(s) and g[i] > s[j]:
                j = j+1
            if j == len(s):
                break
            i=i+1
            j=j+1

        return i