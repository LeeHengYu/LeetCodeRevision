class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def check(cap):
            return sum(min(cap,b) for b in batteries)>=n*cap
            # If one battery can sustain cap mins, then use it throughout
            # Else, combine with other batteries for the whole period
        l, r = 1, 10**14
        res = 0
        while l<=r:
            m=(l+r)//2
            if check(m):
                res = m
                l=m+1
            else:
                r=m-1
        return res
    # O( len(batteries) * log(10**14) )