from math import inf
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        jumps = [0]*(n+1)
        validStart = False
        for i, j in enumerate(ranges):
            left = max(0,i-j)
            if left==0: validStart = True
            right = min(n,i+j)
            jumps[left] = max(jumps[left], right-left)
        if not validStart: return -1
        
        # Jump Game II
        dp = [inf]*(n+1) # see if can reach index n
        dp[0] = 0 
        idx = 0
        while idx<=n:
            reach = jumps[idx]
            for jump in range(1, reach+1):
                if idx+jump>n:
                    break
                dp[idx+jump] = min(dp[idx+jump], 1+dp[idx])
            idx+=1
        return dp[n] if dp[n]!=inf else -1