from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create a Max heap (negative values in Min heap)
        stones = [-s for s in stones]
        heapq.heapify(stones) # O(n)
        
        # Until heap hasnt become empty or has only one element
        # Pop the absolute values of maximum two elements 
        while len(stones)>1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))

            # If not equal, push the difference back in the heap
            # Do reverse subtraction for negative value (Python - Max Heap)
            if first > second:
                heapq.heappush(stones, second - first)
            
        # Append a zero in heap in case the heap has become empty
        stones.append(0)
        return abs(stones[0])