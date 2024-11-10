class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashtext, hashballoon = {}, {}
        for i in range(len(text)):
            hashtext[text[i]] = hashtext.get(text[i], 0) + 1
        for char in "balloon":
            hashballoon[char] = hashballoon.get(char, 0) + 1
        res = len(text)
        for c in hashballoon:
            if c in hashtext:
                res = min(res, hashtext[c]//hashballoon[c])
            else:
                res = 0
        return res

# from collections import Counter
# class Solution:
#     def rearrangeCharacters(self, s: str, target: str) -> int:
#         hashS = Counter(s)
#         hashTarget = Counter(target)

#         res = len(s)
#         for i in hashTarget:
#             res = min(res, hashS[i]//hashTarget[i])
#         return res