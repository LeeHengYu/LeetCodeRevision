import math


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        def comb(n, k):
            return math.factorial(n)//math.factorial(k)//math.factorial(n-k)

        # after the root, the left subtree and right subtree nodes need to be inserted in a certanin order
        # res = [0]
        def dfs(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]
            left = [n for n in arr if n < root]
            right = [n for n in arr if n > root]
            return comb(len(arr)-1, len(left))*dfs(left)*dfs(right)

        return (dfs(nums)-1) % (10**9+7)
