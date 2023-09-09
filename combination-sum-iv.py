class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # similar to coin change
        dp = {}
        def sol(n):
            if n<0: return 0
            if n==0: return 1
            if n in dp: return dp[n]

            res = 0
            for x in nums:
                res += sol(n-x)

            dp[n] = res
            return res
        
        return sol(target)