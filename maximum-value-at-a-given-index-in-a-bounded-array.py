class Solution:
    def maxValue(self, n: int, idx: int, maxSum: int) -> int:

        def cumsum(n):
            return n*(n+1)//2

        def get(LEN, val):
            res = 0
            # [val, val-1, val-2, ..., 1,1,1,1,1]
            remain = LEN-val
            if LEN >= val:
                return cumsum(val)+remain
            else:
                return cumsum(val)-cumsum(val-LEN)

        l, r = 1, maxSum
        lc = idx
        rc = n-1-idx
        res = -1
        while l <= r:
            m = (l+r)//2
            left = get(lc, m-1)
            right = get(rc, m-1)
            total = left+right+m
            if total > maxSum:
                r = m-1
            else:
                res = m
                l = m+1

        return res
