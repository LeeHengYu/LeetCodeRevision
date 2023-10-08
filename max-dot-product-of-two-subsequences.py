from functools import cache
from math import inf
class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        # dp = {}
        @cache
        def dfs(i,j):
            if i>=len(nums1) or j>=len(nums2):
                return -inf
            # if (i,j) in dp: return dp[(i,j)]
            cur = nums1[i]*nums2[j]

            p1 = dfs(i+1, j) 
            p2 = dfs(i, j+1) 
            p3 = dfs(i+1, j+1) 

            res = max(p1, p2, p3, cur+max(p3,0))
            # consider taking the first pair, other numbers are exempted
            # dp[(i,j)] = res
            return res
        return dfs(0,0)