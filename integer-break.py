class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3:
            return n-1
        res = 1
        while n>4: # breaking 4 into 3+1 is not good
            res *= 3
            n -= 3
        res *= n
        return res