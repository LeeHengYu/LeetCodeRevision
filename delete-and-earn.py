from functools import cache
from bisect import bisect_right

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        # delete or not delete - knapsack
        @cache
        def dfs(i):
            if i>=len(nums): return 0
            n = nums[i]
            j = bisect_right(nums, n)
            notTake = dfs(j)
            earned = n*(j-i)

            j = bisect_right(nums, n+1)
            take = earned + dfs(j)
            return max(take, notTake)
        return dfs(0)