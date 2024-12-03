from typing import List

# Hashset Solution -- Less Efficient

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Create a set to store space indices
        spset = set(spaces)
        # Create empty result array
        res = []
        # Iterate through string and input it in result array
        for i,c in enumerate(s):
        # Do not input only if index of space in set 
            if i in spset:
                res.append(" ")
            res.append(c)
        # return join array as a string
        return "".join(res)