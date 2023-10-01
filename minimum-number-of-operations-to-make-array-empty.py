from collections import Counter
from functools import cache

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        @cache
        def help(n):
            if n==0: return (True, 0)
            if n==1: return (False, 10**8)
            if n==2 or n==3: return (True, 1)
            
            p1, t1 = help(n-2)
            p2, t2 = help(n-3)
            if p1 or p2:
                return (True, 1+min(t1,t2))
            return (False, 10**8)
        
        ct = Counter(nums)
        res = 0
        for k in ct.values():
            if not help(k)[0]: return -1
            res += help(k)[1]
        return res