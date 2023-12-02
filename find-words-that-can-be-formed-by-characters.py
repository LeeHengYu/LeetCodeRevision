from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        base = Counter(chars)
        def help(w):
            temp = base.copy()
            for c in w:
                if temp[c] == 0:
                    return 0
                temp[c] -= 1
            return len(w)
        res = 0
        for word in words:
            res += help(word)
        return res