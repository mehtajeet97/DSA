from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Create a Map looping through the string
        count = defaultdict(int)
        for c in s:
            count[c] += 1

        # Iterate through string and find first char in Map whose count is 1
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        
        return -1