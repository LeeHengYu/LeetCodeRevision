class Solution:
    def makeArrayIncreasing(self, arr1: list[int], arr2: list[int]) -> int:
        import bisect
        if len(arr1) == 1:
            return 0

        arr2 = sorted(list(set(arr2)))
        m = len(arr1)
        # [1,5,3,6,7]
        # [1,2,3,4]
        cache = {}

        def solve(i, prev):  # state: (index in arr1, prev)
            if i == m:  # bottom-up base case
                return 0
            if (i, prev) in cache:
                return cache[(i, prev)]

            res = 2001  # inf
            if prev < arr1[i] or not i:
                res = solve(i+1, arr1[i])  # still increasing

            # find the first number in arr2 bigger than prev
            idx = bisect.bisect_right(arr2, prev)
            # if prev >= arr[i-1]
            if idx < len(arr2):
                res = min(res, 1+solve(i+1, arr2[idx]))  # recursion

        # Need to examine if assignment leads to a better result even if it is not necessary
        # DP instead of greedy
            cache[(i, prev)] = res
            return res

        ans = solve(0, -1)
        if ans == 2001:
            return -1
        return ans
