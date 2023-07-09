from collections import Counter
from itertools import permutations
class Solution:
    def largestVariance(self, s: str) -> int:
        count = Counter(s)
        res = 0
        for a, b in permutations(count,2):
            has_a, has_b = 0, 0 #bool
            reA, reB = count[a], count[b]
            opt = 0
            for ch in s:
                if ch==a:
                    opt+=1
                    has_a=1
                    reA-=1
                if ch==b:
                    opt-=1
                    has_b=1
                    reB-=1
                
                if opt<0 and reA and reB:
                    opt=0
                    has_a, has_b = 0, 0

                if has_a and has_b:
                    res = max(res, opt)

        return res