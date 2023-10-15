class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD=10**9+7
        @cache
        def dfs(pos, steps) -> int:
            if steps==pos==0: return 1
            if (pos>steps or pos<0 or pos>=arrLen): return 0 # exception handling
            
            left = dfs(pos-1, steps-1)
            stay = dfs(pos, steps-1)
            right = dfs(pos+1, steps-1)
            return (left+stay+right)%MOD

        return dfs(0,steps)