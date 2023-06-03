class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10001] * (amount+1)
        dp[0] = 0
        
        def solve(i):
            if i<=0:
                return 0

            for coin in coins:
                if i>=coin:
                    dp[i] = min(1+dp[i-coin],dp[i])

        for i in range(1,amount + 1):
            solve(i)

        return dp[amount] if dp[amount]!=10001 else -1