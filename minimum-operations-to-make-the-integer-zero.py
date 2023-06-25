class Solution:
    def makeTheIntegerZero(self, n1: int, n2: int) -> int:
        for k in range(1, 61):
            n1 -= n2
            if n1 <= 0:
                return -1
            count = n1.bit_count()
            if count <= k <= n1:
                return k
        return -1
