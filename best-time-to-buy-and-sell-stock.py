class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        res = 0
        for x in prices:
            lowest = min(lowest, x)
            res = max(res, x-lowest)

        return res