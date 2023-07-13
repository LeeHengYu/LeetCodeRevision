from math import inf
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        res = zero = one = -inf

        for n in arr:
            one = max(zero, n+one) # delete this or already deleted
            zero = max(n, n+zero) # kadane
            res = max(res, one, zero)
        return res