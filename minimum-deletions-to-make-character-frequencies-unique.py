from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        used = set()
        ct = Counter(s)
        res = 0 
        sortedFreq = sorted(ct.values(), reverse=True) # sorting is constant here O(26*log26)
        for f in sortedFreq:
            while f>0 and f in used:
                f-=1
                res+=1
            used.add(f)
        return res 