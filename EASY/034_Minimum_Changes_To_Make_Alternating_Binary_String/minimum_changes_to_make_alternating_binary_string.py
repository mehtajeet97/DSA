class Solution:
    def minOperations(self, s: str) -> int:
        # Assume the string starts with zero
        count = 0
        # Count the changes made at Even and Odd places for alternating
        for i in range(len(s)):
            if i%2: #Odd
                if s[i] == "0":
                    count = count + 1
            else: #Even
                if s[i] == "1":
                    count = count + 1
        # Return the minimum changes to convert into zero or one start string
        return min(count, len(s)-count)
