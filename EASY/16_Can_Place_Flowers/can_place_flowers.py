# Make a new array by placing zeroes at the start and end of array 
# If three consecutive elements are zero, replace middle element by 1

from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0]
        for i in range(1,len(f)-1):
            if f[i-1] == 0 and f[i] == 0 and f[i+1] == 0:
                f[i] = 1
                n = n-1
        return n <= 0