class Solution:
    def soupServings(self, n: int) -> float:
        if n>=4276:
            return 1
        n/=25
        dp = {}
        def dfs(a,b):
            if a<=0 and b>0:
                return 1
            if a<=0 and b<=0:
                return 0.5
            if a>0 and b<=0:
                return 0
            
            if (a,b) in dp:
                return dp[(a,b)]
            res = 0
            res += dfs(a-4,b)
            res += dfs(a-3,b-1)
            res += dfs(a-2,b-2)
            res += dfs(a-1,b-3)
            res *= 0.25
            dp[(a,b)] = res
            return res
        return dfs(n,n)

        # https://leetcode.com/problems/soup-servings/solutions/2188904/python-7-lines-two-versions-t-m-100-100/
        # Threshold 4276 explanation   