class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n=len(nums)
        dp = {}
        def dfs(i, prev):
            if i==n: return 0
            if (i,prev) in dp: return dp[(i,prev)]
            if nums[i]==prev:
                res = dfs(i+1, prev)
            elif nums[i]<prev:
                res = dfs(i+1, prev)+1
            else:
                res = min(
                    dfs(i+1, nums[i]),
                    dfs(i+1, prev)+1
                )
            dp[(i,prev)] = res
            return res
        return dfs(0,0)