class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ct = Counter(s)
        for c in t:
            if ct[c]>0:
                ct[c]-=1
            else:
                return c