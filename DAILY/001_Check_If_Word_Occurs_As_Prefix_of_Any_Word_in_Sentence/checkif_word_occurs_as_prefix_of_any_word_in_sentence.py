class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        for i, w in enumerate(words, start=1):  # Enumerate gives both index and word
            if w.startswith(searchWord):  # Check if the word starts with searchWord
                return i
        return -1  # Return -1 if no word matches