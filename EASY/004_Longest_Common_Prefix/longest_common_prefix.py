# Sort the array which is a list of strings, 
# Take two strings -- first and last
# Loop through each character in the string and check if they are equal
# return when they are inequal
# Until then keep adding the characters of either first or last string into answer (output) string

from typing import List

class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        ans=""
        v=sorted(v)
        first=v[0]
        last=v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 