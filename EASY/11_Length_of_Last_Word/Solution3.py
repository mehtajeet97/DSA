# Single Line Solution -- Has split method which uses whitespace as a delimiter and then pops the last word's length

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split().pop())