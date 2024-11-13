from typing import List
from collections import Counter, defaultdict

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0

        for w in words:
            cur_word = defaultdict(int)
            good = True
            for c in w:
                cur_word[c] += 1
                if c not in count or cur_word[c]>count[c]:
                    good = False
                    break
            if good:
                res += len(w)
        
        return res