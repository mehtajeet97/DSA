from typing import List

# Pointer solution -- More Efficient

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # Create empty result array
        res = []
        # Create a pointer to check values from spaces array
        ptr = 0
        # Iterate through string and insert characters in result
        for i,c in enumerate(s):
        # Add a space when iterator equals pointer value
        # Increment pointer
            if ptr < len(spaces) and i == spaces[ptr]:
                res.append(" ")
                ptr = ptr+1
            res.append(c)
        # Return a joined array as string
        return "".join(res)