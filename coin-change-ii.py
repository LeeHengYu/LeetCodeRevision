class Solution1: # trickier
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0] = 1
        # DP
        for i in range(len(coins)-1,-1,-1): # add available coins one by one
            for j in range(1,amount+1): 
                if j-coins[i]>=0:
                    dp[j] += dp[j-coins[i]]
        return dp[-1]
    
class Solution2: # 2D DP, more straight forward and easier to come up, less efficient in TC and SC
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        n = len(coins)

        def dfs(i, amt):
            if amt<0 or i>=n: return 0
            if not amt: return 1
            if (i,amt) in dp: return dp[(i, amt)]

            res = dfs(i,amt-coins[i]) + dfs(i+1,amt) # pick this coin, jump to next
            dp[(i,amt)]=res
            return res
        return dfs(0,amount)