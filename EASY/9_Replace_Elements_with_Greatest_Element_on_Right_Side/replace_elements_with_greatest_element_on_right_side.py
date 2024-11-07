from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # reverse iteration
        # max = -1
        # new max = max(oldmax, arr[i])
        maxcount = -1
        for i in range(len(arr)-1, -1, -1):
            max_new = max(maxcount, arr[i])
            arr[i] = maxcount
            maxcount = max_new
        return arr