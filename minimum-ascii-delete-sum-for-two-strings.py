class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = {}
        m,n=len(s1), len(s2)
        def dfs(i,j):
            if i==m and j==n:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]

            if i==m:
                res = dfs(i,j+1)+ord(s2[j])
                dp[(i,j)]=res
                return res
            if j==n:
                res = dfs(i+1,j)+ord(s1[i])
                dp[(i,j)]=res
                return res
            if s1[i]==s2[j]:
                res = dfs(i+1,j+1)
            else:
                res = min(dfs(i+1,j)+ord(s1[i]), dfs(i,j+1)+ord(s2[j]))
            dp[(i,j)]=res
            return res

        return dfs(0,0)