from collections import Counter

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        ct = Counter()
        for w in words:
            for c in w:
                ct[c] += 1
        
        for freq in ct.values():
            if freq % len(words): return False
        return True