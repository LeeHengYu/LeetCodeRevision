class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = {}
        def dfs(i):
            if i==n: return True 
            if i==n-1: return 0
            if i in dp: return dp[i]
            
            res1, res2 = False, False
            if i+1<n and nums[i]==nums[i+1]:
                res1 = dfs(i+2)
            if i+2<n and nums[i]==nums[i+1] and nums[i+1]==nums[i+2]:
                res2 = res2 or dfs(i+3)
            if i+2<n and nums[i]==nums[i+1]-1 and nums[i+1]==nums[i+2]-1:
                res2 = res2 or dfs(i+3)
            dp[i] = res1 or res2
            return dp[i]
        return dfs(0)