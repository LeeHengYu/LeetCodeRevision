from math import inf


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # dp
        cache = {}

        def dp(l, h):
            if l >= h:
                return 0
            if (l, h) in cache:
                return cache[(l, h)]

            res = inf
            for i in range(l, h+1):
                res = min(max(dp(l, i-1), dp(i+1, h))+i, res)

            cache[(l, h)] = res
            return res

        return dp(1, n)
