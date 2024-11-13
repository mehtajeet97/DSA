from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]

        for i in range(rowIndex):
            next_row = [0] * (len(res) + 1)

            # Parent Array populates at the same index and index+1
            for j in range(len(res)):
                next_row[j] += res[j]
                next_row[j+1] += res[j]
            res = next_row

        return res

# Formula Based ----> O(N)
# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         base = [1]
#         for i in range(1,rowIndex+1):
#             base.append( int( base[i-1] * (rowIndex-i+1) / i ))
#         return base