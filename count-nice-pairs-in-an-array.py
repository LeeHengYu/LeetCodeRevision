from collections import defaultdict

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        mod = 10**9+7
        res = 0

        def rev(n):
            s = str(n)[::-1]
            return int(s)
            
        for n in nums:
            dif = n - rev(n)
            res += seen[dif]
            seen[dif] += 1
        return res%mod