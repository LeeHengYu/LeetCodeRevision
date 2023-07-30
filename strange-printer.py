class Solution:
    def strangePrinter(self, s: str) -> int:
        # DP memo
        # Subproblem:
        # dp(left,j):
        # if s = "xxxxlenmbxtkx", slide to the x immediately before l
        n = len(s)
        dp = {}
        def dfs(left, right):
            if left>right:
                return 0
            if left==right:
                return 1
            if (left,right) in dp:
                return dp[(left,right)]

            i=left
            while i+1<=right and s[i]==s[i+1]:
                i+=1

            minVal = 1+dfs(i+1,right)
            for j in range(i+2,right+1):
                if s[i]==s[j]:
                    minVal = min(minVal, dfs(i+1,j-1)+dfs(j,right))
            dp[(left,right)] = minVal
            return minVal
        return dfs(0,n-1)