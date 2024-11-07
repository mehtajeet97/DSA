# Loops through each
# Good space complexity but not good on Time

from typing import List
class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        res = ""
        for i in range(len(v[0])):
            for c in v:
                if i== len(c) or c[i] != v[0][i]:
                    return res
            res += v[0][i]
        return res