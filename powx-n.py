class Solution:
    def myPow(self, x: float, n: int) -> float:
        def solve(x,n):
            if not n:
                return 1
            if not x:
                return 0
            res = solve(x,n//2)
            res *= res
            return res*x if n%2 else res
        res = solve(x,abs(n))
        if n<0:
            res = 1/res
        return res