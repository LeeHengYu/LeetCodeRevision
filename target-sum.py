class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # backtracking + DP
        dp = {}
        def dfs(i, cum):
            if i>=len(nums):
                return 1 if cum==target else 0

            if (i,cum) in dp:
                return dp[(i, cum)]

            positive = dfs(i+1, cum+nums[i])
            negative = dfs(i+1, cum-nums[i])
            dp[(i,cum)] = positive + negative
            return positive + negative
        
        return dfs(0,0)