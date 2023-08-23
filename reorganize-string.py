from collections import Counter
from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        ct = Counter(s)
        h = []
        for c in ct:
            heappush(h, [-ct[c],c]) # maxHeap
        res = ""
        q = None
        while len(res)<len(s) and h:
            count, c = heappop(h)
            res += c
            if q and q[0]!=0:
                heappush(h, q)
            q = [count+1, c]
        return res if len(res)==len(s) else ""