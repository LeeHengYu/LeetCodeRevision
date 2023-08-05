class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}
        def dfs(i, hold):
            if i>=n:
                return 0
            if (i, hold) in dp:
                return dp[(i, hold)]

            if hold: # continue holding or sell today
                res = max(dfs(i+1, hold), dfs(i+2, False)+prices[i])
            else: # skip today or buy today
                res = max(dfs(i+1, hold), dfs(i+1, True)-prices[i])
            dp[(i, hold)] = res
            return res
        return dfs(0, False)