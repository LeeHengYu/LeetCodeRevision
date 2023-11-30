from math import floor, log2

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if not n: return 0
        k = floor(log2(n))
        temp = (1<<(k+1))-1 # 2^(k+1) - 1
        return temp - self.minimumOneBitOperations(n^(1<<k))