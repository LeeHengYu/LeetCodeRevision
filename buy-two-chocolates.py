from math import inf
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        c1, c2 = inf, inf
        for p in prices:
            if p<c1:
                c1, c2 = p, c1
            elif c1<=p<c2:
                c2 = p
        left = money - c1 - c2
        return left if left>=0 else money