class Solution1:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit_w = -prices[0]
        profit_wo = 0

        for p in range(1, len(prices)):
            # cash with stocks in hand
            profit_w = max(profit_w, profit_wo-prices[p])
            profit_wo = max(profit_wo, profit_w + prices[p]-fee)  # without
            # here we implicitly allow day trade but since it is never optimal so it won't violate the rule
        return profit_wo
#####################################################################


class Solution2:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # DP memorization
        n = len(prices)
        dp = [[-1, -1] for __ in range(n+1)]
        dp[n][0] = dp[n][1] = 0

        def solve(i, buy):
            if i >= n:
                return 0
            if dp[i][buy] != -1:
                return dp[i][buy]

            if buy:  # can buy or do nothing
                dp[i][buy] = max(solve(i+1, 0) - prices[i], solve(i+1, 1))
            else:  # can sell or do nothing (equivalent to holding)
                dp[i][buy] = max(solve(i+1, 1) + prices[i] -
                                 fee, solve(i+1, 0))

            return dp[i][buy]

        for i in range(n-1, -1, -1):
            for j in range(2):
                solve(i, j)
        return dp[0][1]
