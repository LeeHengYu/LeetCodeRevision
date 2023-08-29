# Morgan Stanley 2023 Tech X Challenge question

# class Solution: (TLE)
#     @cache
#     def superEggDrop(self, k: int, n: int) -> int:
#         if n==0 or n==1 or k==1: return n
#         res = 10001
#         for i in range(1,n+1):
#             temp = max(self.superEggDrop(k-1, i-1), # break
#                        self.superEggDrop(k  , n-i)
#                     )+1
#             res = min(res, temp)
#         return res

# Binary Search solution
from functools import cache

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        @cache
        def dp(k,n):
            if n<=0 or k==1: return n 
            res = 100000
            l, r= 1, n

            while l<=r:
                m = (l+r)//2
                left = dp(k, n-m)
                right = dp(k-1, m-1)
                temp = 1+max(right, left)
                res = min(temp, res)
                # Tricky part:
                # need the worst case
                if right>left:
                    r = m-1
                else:
                    l = m+1
            return res
        return dp(k,n)