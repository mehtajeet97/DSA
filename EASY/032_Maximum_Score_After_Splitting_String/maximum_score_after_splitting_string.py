class Solution:
    def maxScore(self, s: str) -> int:
        zeroCount = 0
        # Count ones in the string
        oneCount = s.count("1")
        res = 0
        # Check every element until second last
        for i in range(len(s)-1):
            # Element zero increases zerocount, element One reduces Onecount
            if s[i] == "0":
                zeroCount = zeroCount + 1
            else:
                oneCount = oneCount - 1

            res = max(res, zeroCount + oneCount)

        return res
