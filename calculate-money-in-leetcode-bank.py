class Solution:
    def totalMoney(self, n: int) -> int:
        F = n//7
        R = n%7
        def f(n):
            return n*(n+1)//2
        if not F:
            return f(n)
        FULL = F*f(7)+7*f(F-1)
        RE = F*R + f(R)
        return FULL+RE