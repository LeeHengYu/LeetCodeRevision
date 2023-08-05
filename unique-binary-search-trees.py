class Solution:
    def numTrees(self, n: int) -> int:
        # DP
        res = 0
        dp = defaultdict(int)
        def sol(left,right):
            if left>=right:
                return 1
            if (left,right) in dp:
                return dp[(left,right)]
            res = 0
            for i in range(left,right+1):
                l = sol(left, i-1)
                r = sol(i+1, right)
                res += (l*r)
            dp[(left,right)]=res
            return res
        return sol(1,n)