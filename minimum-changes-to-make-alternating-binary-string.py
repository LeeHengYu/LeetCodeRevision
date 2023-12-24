class Solution:
    def minOperations(self, s: str) -> int:
        res = 0
        cur = 0
        for c in s:
            if cur != int(c):
                res += 1
            cur ^= 1 
        return min(res, len(s)-res)