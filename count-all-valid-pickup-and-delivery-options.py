from math import factorial

class Solution1:
    def countOrders(self, n: int) -> int:
        if n==1: return 1
        return n*(2*n-1)*self.countOrders(n-1) % (10**9+7)


class Solution2:
    def countOrders(self, n: int) -> int:
        if n==1: return 1
        a = factorial(2*n)
        return a//(2**n) % (10**9+7)