class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        profit_w = -prices[0]
        profit_wo = 0

        for p in range(1, len(prices)):
            # cash with stocks in hand
            profit_w = max(profit_w, profit_wo-prices[p])
            profit_wo = max(profit_wo, profit_w + prices[p]-fee)  # without
            # here we implicitly allow day trade but since it is never optimal so it won't violate the rule
        return profit_wo
